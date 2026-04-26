import os
import json
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from agent import SOC2Agent
from scenarios import auditors, targets, risk_profiles

load_dotenv()

app = Flask(__name__)
api_key = os.getenv("TOKENROUTER_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "tokenrouter_configured": bool(api_key)
    })

@app.route("/api/collect", methods=["POST"])
def collect():
    try:
        if not api_key:
            return jsonify({
                "success": False,
                "error": "TokenRouter API key not configured"
            }), 500

        data = request.get_json() or {}
        demo_mode = data.get('demo_mode', True)
        auditor_id = data.get('auditor', 'healthcare')
        target_id = data.get('target', 'salesforce')
        risk_profile = data.get('risk_profile', 'healthy')

        auditor = auditors.get(auditor_id, {})
        target = targets.get(target_id, {})
        profile = risk_profiles.get(risk_profile, {})

        agent = SOC2Agent(api_key, demo_mode=demo_mode, auditor=auditor, target=target)
        result = agent.collect_evidence()

        return jsonify(result)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    if not api_key:
        print("WARNING: TOKENROUTER_API_KEY not set in .env file")
    print("Starting SOC 2 Evidence Collector...")
    print("Open http://localhost:5001 in your browser")
    app.run(host="0.0.0.0", port=5001, debug=True)
