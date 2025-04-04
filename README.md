PII Log Analyser – Fullstack GenAI-Powered Tool

A complete GenAI-driven tool to detect and score PII in logs, auto-redact, sync reports to a React dashboard, trigger Telegram alerts, and visualize everything in real time.

---

## 📁 Project Structure

pii-detector/ ├── log_analyzer.py         # Main script: scan, redact, score, sync, archive ├── logs/                   # Raw input logs (.txt) ├── output/                 # Generated reports (JSON, CSV, MD) ├── archive/                # Archived logs (timestamped + zipped) ├── sync.sh                 # Copies reports to React dashboard ├── run_all.sh              # Executes scanner + dashboard in one tap └── pii-dashboard/          # React dashboard (localhost:3002)

---

## ✅ Quickstart (One-Liner)

```bash
cd ~/pii-detector && ./run_all.sh

This will:

Scan logs in logs/

Generate reports in output/

Archive processed logs to archive/

Sync reports to dashboard

Launch React UI in your browser

Start React server on localhost:3002



---

⚙️ Features

GPT-based detection of:

Emails, phone numbers, card numbers, IPs


Risk scoring: High / Medium / Low

Log redaction + Markdown summary

JSON / CSV / MD report export

Telegram alert (high-risk findings)

Weekly log ZIP archive (on Sundays)

Auto-sync to dashboard

Auto-open in browser

One-touch launcher via run_all.sh



---

🖥️ Dashboard

Location: http://localhost:3002
Auto-launched via termux-open-url when scan completes.

Displays:

Risk pie chart

Color-coded PII table

Supports live synced .json reports



---

🛠️ Manual Options

Run scanner only:

python log_analyzer.py

Sync reports manually:

./sync.sh

Start dashboard manually:

cd pii-dashboard
npm start -- --host 0.0.0.0 --port 3002


---

🔮 Future Enhancements

Upload ZIP to cloud or email weekly

Redacted log preview in dashboard

Log search/filter in UI

Multi-user access and project tagging

FastAPI backend integration



---

Built in Termux using GenAI. Works 100% offline and local.