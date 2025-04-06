# PII Log Analyser — GenAI + Dashboard Powered Privacy Tool

A lightweight and fully local privacy tool to scan log files for Personally Identifiable Information (PII), score their risk, and view results in a React dashboard.

---

## 🔧 Features

- **GenAI-powered log scanning**
- Detects PII like emails, phone numbers, IPs, PANs, card numbers
- **Risk scoring**: High / Medium / Low
- **Batch scan support** via logs folder
- **Redacts sensitive data** from raw logs
- **CSV, JSON, Markdown reports**
- **Live React dashboard** to visualize findings
- **Telegram alerts** for high-risk PII
- **Auto-archive** scanned logs
- **Works 100% in Termux** (Android)

---

## ▶️ How to Use

### 1. Clone the repo

```bash
git clone https://github.com/mayanklau/PII-Log-analyser.git
cd PII-Log-analyser

2. Install dependencies (Python + Node)

pip install -r requirements.txt
cd pii-dashboard
npm install --legacy-peer-deps

3. Run a sample scan

cd ~/pii-detector
echo "Email: test@example.com, Card: 4111-1111-1111-1111" > logs/test_input.txt
python log_analyzer.py
cp output/test_input_report.json pii-dashboard/public/data/

4. Start the dashboard

cd pii-dashboard
npm start -- --host 0.0.0.0 --port 3002

Then open http://192.168.x.x:3002 in Chrome
(Replace with your local IP — use ip route | grep wlan0 to find it)


---

⚙️ Upcoming Enhancements

[ ] Auto-pick latest report file

[ ] Export dashboard as PDF

[ ] Filter by High / Medium / Low risk

[ ] Multi-log timeline view

[ ] Dark mode toggle



---

🤖 Built With

Python (Log Scanner)

OpenAI API

React + Chart.js

Termux on Android



---

> Designed and built by Mayank lau

---

## 🎬 Demo Video

Click the link below to view the full demo of the PII Log Analyser:

**[▶️ Download or watch demo video (MP4)](https://github.com/mayanklau/PII-Log-analyser/blob/main/demo.mp4?raw=true)**
