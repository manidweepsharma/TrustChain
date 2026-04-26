auditors = {
    "healthcare": {
        "name": "MediCare Systems",
        "type": "Healthcare Provider",
        "description": "HIPAA-regulated healthcare organization"
    },
    "financial": {
        "name": "SecureBank Ltd",
        "type": "Financial Services",
        "description": "Regulated financial institution"
    },
    "ecommerce": {
        "name": "RetailTech Corp",
        "type": "E-Commerce Company",
        "description": "Large online retailer"
    },
    "legal": {
        "name": "LawFlow Partners",
        "type": "Legal Firm",
        "description": "Enterprise legal services"
    },
    "manufacturing": {
        "name": "IndustrialOps Inc",
        "type": "Manufacturing",
        "description": "Industrial manufacturing company"
    }
}

targets = {
    "salesforce": {
        "name": "Salesforce CRM",
        "type": "CRM Platform",
        "description": "Customer relationship management system"
    },
    "aws": {
        "name": "AWS Infrastructure",
        "type": "Cloud Services",
        "description": "Amazon Web Services cloud platform"
    },
    "slack": {
        "name": "Slack Enterprise",
        "type": "Communication Platform",
        "description": "Team collaboration and messaging"
    },
    "stripe": {
        "name": "Stripe Payments",
        "type": "Payment Processor",
        "description": "Payment processing platform"
    },
    "okta": {
        "name": "Okta Identity",
        "type": "Identity Management",
        "description": "Identity and access management"
    },
    "github": {
        "name": "GitHub Enterprise",
        "type": "Code Repository",
        "description": "Source code management platform"
    },
    "docusign": {
        "name": "DocuSign eSignature",
        "type": "Document Management",
        "description": "Electronic signature and document platform"
    },
    "tableau": {
        "name": "Tableau Analytics",
        "type": "Analytics Platform",
        "description": "Business intelligence and analytics"
    }
}

risk_profiles = {
    "healthy": {
        "name": "Healthy Company",
        "description": "Strong compliance posture, minimal findings",
        "total_members": 52,
        "admin_count": 4,
        "inactive_accounts": [],
        "mfa_enabled_users": 52,
        "mfa_disabled_users": 0,
        "access_last_reviewed": "2026-04-20",
        "security_training_completed": 52,
        "total_training": 52,
        "expected_findings": 0,
        "risk_level": "LOW"
    },
    "needs_improvement": {
        "name": "Needs Improvement",
        "description": "Multiple findings, requires immediate attention",
        "total_members": 28,
        "admin_count": 8,
        "inactive_accounts": ["contractor_old", "intern_2023", "temp_vendor"],
        "mfa_enabled_users": 22,
        "mfa_disabled_users": 6,
        "access_last_reviewed": "2026-02-15",
        "security_training_completed": 18,
        "total_training": 28,
        "expected_findings": 5,
        "risk_level": "HIGH"
    },
    "post_incident": {
        "name": "Post-Incident Recovery",
        "description": "Recovering from security incident, implementing controls",
        "total_members": 95,
        "admin_count": 15,
        "inactive_accounts": ["breach_account_1", "breach_account_2", "breach_account_3"],
        "mfa_enabled_users": 85,
        "mfa_disabled_users": 10,
        "access_last_reviewed": "2026-03-01",
        "security_training_completed": 75,
        "total_training": 95,
        "expected_findings": 8,
        "risk_level": "HIGH"
    },
    "startup": {
        "name": "Early-Stage Startup",
        "description": "Basic security controls, growing infrastructure",
        "total_members": 15,
        "admin_count": 5,
        "inactive_accounts": [],
        "mfa_enabled_users": 12,
        "mfa_disabled_users": 3,
        "access_last_reviewed": "2026-04-01",
        "security_training_completed": 10,
        "total_training": 15,
        "expected_findings": 3,
        "risk_level": "MEDIUM"
    },
    "enterprise": {
        "name": "Large Enterprise",
        "description": "Complex access management, multiple teams",
        "total_members": 342,
        "admin_count": 28,
        "inactive_accounts": ["old_emp_1", "contractor_expired"],
        "mfa_enabled_users": 338,
        "mfa_disabled_users": 4,
        "access_last_reviewed": "2026-04-15",
        "security_training_completed": 330,
        "total_training": 342,
        "expected_findings": 2,
        "risk_level": "LOW"
    },
    "non_compliant": {
        "name": "Non-Compliant Organization",
        "description": "Critical security gaps, urgent remediation needed",
        "total_members": 45,
        "admin_count": 18,
        "inactive_accounts": ["user1", "user2", "user3", "user4", "user5"],
        "mfa_enabled_users": 20,
        "mfa_disabled_users": 25,
        "access_last_reviewed": "2025-10-01",
        "security_training_completed": 15,
        "total_training": 45,
        "expected_findings": 12,
        "risk_level": "CRITICAL"
    },
    "recovering": {
        "name": "Remediation in Progress",
        "description": "Addressing previous audit findings",
        "total_members": 73,
        "admin_count": 7,
        "inactive_accounts": ["old_contractor"],
        "mfa_enabled_users": 68,
        "mfa_disabled_users": 5,
        "access_last_reviewed": "2026-03-20",
        "security_training_completed": 60,
        "total_training": 73,
        "expected_findings": 4,
        "risk_level": "MEDIUM"
    },
    "perfect": {
        "name": "Perfect Compliance",
        "description": "All controls operational and effective",
        "total_members": 89,
        "admin_count": 5,
        "inactive_accounts": [],
        "mfa_enabled_users": 89,
        "mfa_disabled_users": 0,
        "access_last_reviewed": "2026-04-22",
        "security_training_completed": 89,
        "total_training": 89,
        "expected_findings": 0,
        "risk_level": "LOW"
    }
}
