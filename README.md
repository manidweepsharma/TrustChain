# SOC 2 Evidence Collector AI Agent

A Flask web application that uses TokenRouter to orchestrate multiple AI models (GPT-4, Claude 3.5 Sonnet, Gemini 2.0 Flash) to automate compliance evidence gathering for SOC 2 audits.

## Features

- **Multi-Model Orchestration**: Leverages GPT-4 for data extraction, Claude for risk analysis, and Gemini for report generation
- **Automated Evidence Collection**: Gathers mock data from GitHub, AWS, and Slack
- **Real-time Status Updates**: Live feedback during processing
- **Professional UI**: Clean, modern web interface with gradient design
- **Downloadable Reports**: Package all evidence into a text file

## Architecture

```
SOC 2 Evidence Collector
├── Backend: Flask (Python)
│   ├── agent.py: SOC2Agent orchestration logic
│   └── app.py: Flask routes and server
├── Frontend: Vanilla HTML/CSS/JavaScript
│   └── templates/index.html: Web UI
└── API: TokenRouter (OpenAI-compatible)
    ├── GPT-4: Data extraction
    ├── Claude 3.5 Sonnet: Risk analysis
    └── Gemini 2.0 Flash: Report generation
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- TokenRouter API key (from https://bit.ly/4eG9ddG)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Edit `.env` and add your TokenRouter API key:
```
TOKENROUTER_API_KEY=your_actual_key_here
```

### 4. Run the Application
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 5. Open in Browser
Navigate to `http://localhost:5000` and click "Collect Evidence" to start the pipeline.

## How It Works

### Pipeline Stages

1. **Data Gathering** (Mock Data)
   - GitHub: Organization members, MFA status, inactive accounts
   - AWS: IAM policies, MFA compliance, access review dates
   - Slack: Security training completion, phishing test results

2. **Data Extraction (GPT-4)**
   - Processes raw data into structured JSON metrics
   - Extracts key compliance indicators
   - Returns: total_users, admin_percentage, mfa_compliance_rate, etc.

3. **Risk Analysis (Claude 3.5 Sonnet)**
   - Acts as SOC 2 compliance auditor
   - Identifies stale accounts, admin ratio concerns, MFA gaps
   - Assigns risk levels (HIGH/MEDIUM/LOW)
   - Returns: Detailed compliance findings

4. **Report Generation (Gemini 2.0 Flash)**
   - Creates formal audit-ready documentation
   - Includes: Executive Summary, Evidence, Assessment, Findings, Recommendations
   - Returns: Professional audit report with all sections

### API Integration

All models are called via TokenRouter at `https://api.tokenrouter.com/v1/chat/completions`

**Model Names**:
- `gpt-4` - Data extraction
- `claude-3-5-sonnet-20241022` - Risk analysis
- `gemini-2.0-flash-exp` - Report generation

## Testing

1. Start the server: `python app.py`
2. Open http://localhost:5000
3. Click "Collect Evidence"
4. Monitor status updates in real-time
5. Review results in three sections
6. Download evidence package

## Error Handling

- API failures are caught and gracefully reported
- Status updates show all errors
- Fallback logic provides realistic mock data if models fail
- Server continues running even if individual API calls fail

## Project Structure

```
soc2-agent/
├── app.py                  # Flask application
├── agent.py                # SOC2Agent class and orchestration
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (API keys)
├── README.md              # This file
└── templates/
    └── index.html         # Web UI
```

## Security Notes

- Never commit `.env` file with real API keys
- TokenRouter API key should be kept confidential
- All mock data is safe for demonstration purposes
- No real data is collected from actual services

## Success Criteria

✅ Flask server starts without errors
✅ All 3 models (GPT-4, Claude, Gemini) are called successfully
✅ Status updates appear in real-time
✅ Results display in 3 separate sections
✅ Error handling works gracefully
✅ UI looks professional and responsive
✅ Evidence package can be downloaded

## Future Enhancements

- Real integration with GitHub, AWS, Slack APIs
- Database storage for audit history
- Custom report templates
- Multi-control compliance checks
- Team collaboration features
- Export to PDF/Word formats

## Support

For issues with TokenRouter API, visit: https://bit.ly/4eG9ddG
For Flask documentation: https://flask.palletsprojects.com/
