# PII Log Analyser – Fullstack GenAI Tool

This fullstack tool scans logs for PII using GenAI, assigns risk levels, sends Telegram alerts, and visualizes the results via a React dashboard.

---

## 📁 Project Structure

pii-detector/ ├── log_analyzer.py         # Python script: scans logs, exports reports ├── logs/                   # Raw input logs ├── output/                 # JSON, CSV, and Markdown reports ├── archive/                # Archived scanned logs (timestamped) ├── sync.sh                 # Sync script: copies reports to dashboard └── pii-dashboard/          # React app to visualize PII findings

---

## ✅ How to Use

### 1. Drop Logs to Be Scanned

```bash
cd ~/pii-detector
echo "Email: user@example.com, Card: 4111-1111-1111-1111" > logs/sample.txt


---

2. Run Full Workflow (Scanner + Sync + Dashboard)

cd ~/pii-detector && python log_analyzer.py && ./sync.sh && cd pii-dashboard && npm start


---

3. Open the Dashboard

Open this in your browser:

http://localhost:3002

Or:

termux-open-url http://localhost:3002

You’ll see:

A pie chart for High / Medium / Low risk breakdown

A color-coded table of PII items



---

🔄 Syncing Reports

After each scan, sync JSON reports to the dashboard:

./sync.sh


---

⚙️ Features

GPT-based PII detection

High/Medium/Low risk scoring

Markdown + CSV + JSON reports

Telegram alerts for High-risk PII

Auto-archive scanned logs

Weekly ZIP compression of archives

React dashboard with charts and tables



---

✅ Future Roadmap

Auto-upload weekly ZIP to cloud/email

Live FastAPI integration (no file sync needed)

Redacted log viewer in dashboard

Dashboard filters and sorting



---

Built with Termux, GenAI, and a no-code mindset.
