✅ Full README.md (Updated for April 2025)

# PII Log Analyzer (GPT-powered, Mobile-Ready)

A GenAI-powered Python tool to automatically detect, score, redact, and report exposed PII in logs — fully portable and runs even inside **Termux** on Android.

---

## 🔍 What It Does

- Detects PII (emails, phones, card numbers, IPs, etc.)
- Tags findings with **High / Medium / Low** risk levels
- Generates:
  - Markdown reports (`.md`)
  - JSON exports (`.json`)
  - CSV exports (`.csv`)
- Creates a **redacted copy** of logs with masked PII
- Pushes findings to GitHub automatically
- Runs daily via Termux `cron`

---

## ⚙️ How It Works

1. Load production or dev logs into `sample_logs.txt`
2. Run:
   ```bash
   python log_analyzer.py

3. The tool:

Uses OpenAI GPT to detect PII

Scores and categorizes each item

Creates redacted logs (redacted_logs.txt)

Saves outputs as pii_report_1.md, pii_report.csv, pii_report.json

Automatically pushes results to GitHub





---

🔐 Secure by Design

OpenAI API Key stored via environment variable (OPENAI_API_KEY)

GitHub pushes use Personal Access Tokens (PAT)

No secrets hardcoded

Safe to run in mobile or cloud setups



---

🗓 Daily Auto Scan (via Cron)

Enabled using Termux's built-in cron:

crontab -e

Example cron job:

0 9 * * * cd ~/pii-detector && python log_analyzer.py >> cron_log.txt 2>&1



---

📁 Output Example

pii_report_1.md: Human-readable risk-based summary

redacted_logs.txt: Masked version of your original logs

pii_report.csv: Structured tabular format

pii_report.json: Ready for dashboard/analytics pipelines



---

🛠 Requirements

Python 3 (Termux or any Linux/macOS)

OpenAI API key (GPT-3.5+)

Git installed and configured



---

🚀 Future Enhancements

Telegram alert integration

Log type auto-detection (Apache, Nginx, etc.)

Weekly ZIP archive of all reports

Streamlit Web UI (optional)



---

🤖 Demo

> Built and tested entirely inside Termux on Android.




---

🔗 Repository

github.com/mayanklau/PII-Log-analyser
