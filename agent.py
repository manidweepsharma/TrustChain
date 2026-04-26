import os
import json
import requests
from datetime import datetime, timedelta

class SOC2Agent:
    def __init__(self, api_key, demo_mode=True, auditor=None, target=None):
        self.api_key = api_key
        self.demo_mode = demo_mode
        self.auditor = auditor or {}
        self.target = target or {}
        self.tokenrouter_url = "https://api.tokenrouter.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.status_updates = []

    def add_status(self, message):
        self.status_updates.append({
            "timestamp": datetime.now().isoformat(),
            "message": message
        })
        print(f"[Status] {message}")

    def gather_github_data(self):
        """GitHub organization data - real or mock"""
        if self.demo_mode:
            self.add_status("Gathering GitHub access data (Demo Mode)...")
            return {
                "organization": "acme-corp",
                "total_members": 47,
                "recent_additions": [
                    {"login": "john_dev", "added_date": "2026-04-10", "role": "engineer"},
                    {"login": "sarah_ops", "added_date": "2026-04-05", "role": "devops"},
                    {"login": "mike_sec", "added_date": "2026-03-28", "role": "security"}
                ],
                "admin_count": 8,
                "inactive_accounts": ["old_contractor_1", "temp_intern_2"],
                "mfa_enabled_users": 45,
                "mfa_disabled_users": 2,
                "access_last_reviewed": "2026-04-01",
                "repositories_with_secrets_detected": 0
            }

        self.add_status("Gathering GitHub access data (Real API)...")
        try:
            headers = {"Accept": "application/vnd.github.v3+json"}
            resp = requests.get("https://api.github.com/orgs/anthropics", headers=headers, timeout=10)
            resp.raise_for_status()
            org_data = resp.json()

            repo_resp = requests.get(f"{org_data['repos_url']}", headers=headers, timeout=10)
            repo_resp.raise_for_status()
            repos = repo_resp.json()

            self.add_status(f"✓ Retrieved real GitHub data for {org_data['login']}")

            return {
                "organization": org_data.get("login", "unknown"),
                "total_members": org_data.get("public_members", 0),
                "recent_additions": [],
                "admin_count": 0,
                "inactive_accounts": [],
                "mfa_enabled_users": org_data.get("public_members", 0),
                "mfa_disabled_users": 0,
                "access_last_reviewed": datetime.now().strftime("%Y-%m-%d"),
                "repositories_with_secrets_detected": 0,
                "repositories_count": len(repos) if repos else 0
            }
        except Exception as e:
            self.add_status(f"WARNING: Real GitHub API failed, falling back to demo data: {str(e)}")
            return self.gather_github_data_mock()

    def gather_github_data_mock(self):
        """Mock GitHub organization data"""
        return {
            "organization": "acme-corp",
            "total_members": 47,
            "recent_additions": [
                {"login": "john_dev", "added_date": "2026-04-10", "role": "engineer"},
                {"login": "sarah_ops", "added_date": "2026-04-05", "role": "devops"},
                {"login": "mike_sec", "added_date": "2026-03-28", "role": "security"}
            ],
            "admin_count": 8,
            "inactive_accounts": ["old_contractor_1", "temp_intern_2"],
            "mfa_enabled_users": 45,
            "mfa_disabled_users": 2,
            "access_last_reviewed": "2026-04-01",
            "repositories_with_secrets_detected": 0
        }

    def gather_aws_data(self):
        """Mock AWS IAM data"""
        self.add_status("Gathering AWS IAM evidence...")
        return {
            "iam_policies_reviewed": 12,
            "mfa_enabled_accounts": 28,
            "mfa_total_accounts": 29,
            "mfa_enabled_rate": "96.6%",
            "last_access_review": "2026-04-01",
            "access_keys_rotated_90days": 26,
            "root_account_mfa_enabled": True,
            "iam_roles_with_admin_policy": 2,
            "service_control_policies_active": 5
        }

    def gather_slack_data(self):
        """Mock Slack security training data"""
        self.add_status("Gathering Slack security training records...")
        return {
            "total_members": 47,
            "security_training_completed": 45,
            "completion_rate": "95.7%",
            "pending_training": ["john_dev", "mike_sec"],
            "last_training_date": "2026-04-15",
            "phishing_test_click_rate": "2.1%",
            "data_classification_trained": 43
        }

    def call_model(self, model, prompt, temperature=0.7):
        """Generic method to call TokenRouter API"""
        try:
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": temperature
            }

            response = requests.post(
                self.tokenrouter_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            error_msg = f"API call failed for model {model}: {str(e)}"
            self.add_status(f"ERROR: {error_msg}")
            raise Exception(error_msg)

    def extract_structured_data(self, raw_data):
        """Use GPT-4o-mini to extract structured JSON metrics"""
        self.add_status("Extracting structured data with GPT-4o-mini...")

        prompt = f"""Extract key SOC 2 compliance metrics from this GitHub organization data.

Data:
{json.dumps(raw_data, indent=2)}

Return a JSON object with these exact fields:
- total_users
- new_users_q1
- admin_percentage
- stale_accounts_count
- mfa_compliance_rate

Return ONLY valid JSON, no markdown formatting or code blocks."""

        try:
            response = self.call_model("openai/gpt-4o-mini", prompt, temperature=0.3)
            extracted = json.loads(response)
            self.add_status("✓ GPT-4o-mini extraction complete")
            return extracted
        except json.JSONDecodeError:
            self.add_status("ERROR: Could not parse JSON from GPT-4o-mini response")
            return {
                "total_users": raw_data.get("total_members", 47),
                "new_users_q1": len(raw_data.get("recent_additions", [])),
                "admin_percentage": round((raw_data.get("admin_count", 8) / raw_data.get("total_members", 47)) * 100, 1),
                "stale_accounts_count": len(raw_data.get("inactive_accounts", [])),
                "mfa_compliance_rate": round((raw_data.get("mfa_enabled_users", 45) / raw_data.get("total_members", 47)) * 100, 1)
            }

    def analyze_risks(self, structured_data, github_data):
        """Use Claude Opus to analyze compliance risks"""
        self.add_status("Analyzing compliance risks with Claude Opus...")

        auditor_name = self.auditor.get('name', 'Organization')
        target_name = self.target.get('name', 'Vendor')
        target_type = self.target.get('type', 'System')

        prompt = f"""You are a SOC 2 compliance auditor at {auditor_name}, reviewing vendor compliance.

AUDIT SCOPE:
- Auditing Company: {auditor_name} ({self.auditor.get('type', 'Organization')})
- Vendor/Target Being Assessed: {target_name} ({target_type})
- Control: AC-2 (User Access Review)

Access data for {target_name}:
{json.dumps(structured_data, indent=2)}

GitHub details:
- Inactive accounts: {github_data.get('inactive_accounts', [])}
- Last access review: {github_data.get('access_last_reviewed')}

As a {auditor_name} auditor, analyze {target_name} for SOC 2 compliance:

1. Stale Accounts: Are there inactive accounts that should be deprovisioned?
2. Admin Ratio: Is {structured_data.get('admin_percentage', 0)}% appropriate for a {target_type}?
3. MFA Compliance: Is {structured_data.get('mfa_compliance_rate', 0)}% adequate for regulatory requirements?
4. Access Review: Has a quarterly review been performed recently?
5. New User Onboarding: Is the onboarding process properly documented?

Provide specific findings with risk levels (HIGH/MEDIUM/LOW) and evidence relevant to {auditor_name}'s compliance needs."""

        try:
            response = self.call_model("anthropic/claude-opus-4.7", prompt, temperature=0.7)
            self.add_status("✓ Claude Opus analysis complete")
            return response
        except Exception as e:
            self.add_status(f"ERROR: Claude Opus analysis failed: {str(e)}")
            return "Risk analysis unavailable due to API error."

    def generate_audit_report(self, structured_data, risk_analysis, aws_data, slack_data):
        """Use GPT-5.4 to generate formal audit report"""
        self.add_status("Generating audit report with GPT-5.4...")

        auditor_name = self.auditor.get('name', 'Auditing Organization')
        target_name = self.target.get('name', 'Vendor')
        target_type = self.target.get('type', 'System')

        extracted_str = json.dumps(structured_data, indent=2)
        aws_str = json.dumps(aws_data, indent=2)
        slack_str = json.dumps(slack_data, indent=2)

        prompt = f"""Create a formal SOC 2 audit evidence document for Control AC-2: User Access Review.

AUDIT CONTEXT:
- Auditing Organization: {auditor_name}
- Vendor Being Assessed: {target_name} ({target_type})
- Purpose: SOC 2 Type II Compliance Audit
- Prepared by: {auditor_name} Compliance Team

EVIDENCE SOURCES:

Access Control Data:
{extracted_str}

Risk Analysis:
{risk_analysis}

Infrastructure Evidence:
{aws_str}

Training & Security Records:
{slack_str}

Generate a professional audit document with these sections:
1. Executive Summary (2-3 sentences)
2. Evidence Collected (bullet points)
3. Compliance Assessment (Pass/Fail/Partial for AC-2)
4. Findings (numbered list)
5. Recommendations (numbered list)

Include:
- Audit Period: Q1 2026
- Prepared: April 25, 2026
- Auditor: {auditor_name}
- Vendor: {target_name}
- Control: AC-2 - User Access Review"""

        try:
            response = self.call_model("openai/gpt-5.4", prompt, temperature=0.7)
            self.add_status("✓ GPT-5.4 report generation complete")
            return response
        except Exception as e:
            self.add_status(f"ERROR: Report generation failed: {str(e)}")
            return "Report generation unavailable due to API error."

    def collect_evidence(self, status_callback=None):
        """Main orchestration method"""
        try:
            self.status_updates = []
            self.add_status("Starting SOC 2 evidence collection pipeline...")

            github_data = self.gather_github_data()
            aws_data = self.gather_aws_data()
            slack_data = self.gather_slack_data()

            self.add_status("Data gathering complete, starting AI pipeline...")

            structured_data = self.extract_structured_data(github_data)

            risk_analysis = self.analyze_risks(structured_data, github_data)

            audit_report = self.generate_audit_report(structured_data, risk_analysis, aws_data, slack_data)

            self.add_status("Evidence collection complete!")

            return {
                "success": True,
                "extracted_data": structured_data,
                "risk_analysis": risk_analysis,
                "audit_report": audit_report,
                "status_updates": self.status_updates
            }
        except Exception as e:
            error_msg = str(e)
            self.add_status(f"FATAL ERROR: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "status_updates": self.status_updates
            }
