PII Log Analyser – Fullstack GenAI Tool

This is a fullstack GenAI-based tool that scans production logs for exposed PII, scores risk levels, sends alerts, and displays results on a React dashboard.

---

## 📁 Project Structure

pii-detector/ ├── log_analyzer.py         # Python script to detect & score PII ├── logs/                   # Raw input logs ├── output/                 # Reports (.json / .csv / .md) ├── archive/                # Processed logs with timestamps ├── sync.sh                 # Script to sync output → dashboard └── pii-dashboard/          # React frontend to visualize reports

---

## ⚙️ 1. Run the PII Detection (Python backend)

```bash
cd ~/pii-detector
echo "Email: user@example.com, Card: 4111-1111-1111-1111" > logs/test.txt
python log_analyzer.py

This will:

Detect PII from logs/

Generate reports in output/

Archive logs

Send Telegram alerts for high-risk

Auto-push to GitHub



---

🔄 2. Sync Reports to Frontend

cd ~/pii-detector
./sync.sh

This will:

Copy all .json reports from output/ to pii-dashboard/public/data/



---

📊 3. Launch the Dashboard (React frontend)

cd ~/pii-detector/pii-dashboard
npm install   # only first time
npm start

Now open:
http://localhost:3000 in your browser

You’ll see:

A risk summary pie chart

A color-coded PII table



---

✅ Features

PII Detection via GPT (emails, phones, cards, IPs)

High/Medium/Low risk scoring

Markdown + CSV + JSON report export

Auto redaction in logs

Telegram alerts for high-risk PII

Auto-archive and weekly ZIP backup

React dashboard for visualization

Fully local + GitHub versioned



---

✅ Future Add-ons

Email or cloud upload of weekly ZIPs

Live API integration (FastAPI backend)

Search/filter by PII type or date

User-upload interface via dashboard



---

Made in Termux with GenAI and Zero Manual Coding.

