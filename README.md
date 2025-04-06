# GenAI-Powered PII Log Analyser

A mobile-first GenAI tool built using **Termux** to scan logs for **PII (Personally Identifiable Information)**, classify by risk, and auto-sync results to a visual dashboard — with alerts, automation, and reporting built-in.

---

## 🎬 Demo Video

Watch the tool in action:  
[▶️ Watch the demo on YouTube](https://youtu.be/kR_bo8nmGw8)

Or click the image below:

[![Watch the demo on YouTube](https://img.youtube.com/vi/kR_bo8nmGw8/hqdefault.jpg)](https://youtu.be/kR_bo8nmGw8)

---

## ✅ Features

- Scan logs with Python + RegEx + GPT
- Classify PII (email, phone, card, IP, etc.) by **risk level**
- Auto-generate reports in `.md`, `.csv`, `.json`
- Archive redacted logs automatically
- Push results to a **React dashboard**
- Daily scan scheduler with `cron`
- Telegram alerts for **high-risk PII**
- Batch processing support
- Built entirely on mobile (Termux)

---

## 🧪 Sample Output

```text
Email: test@example.com — Medium
Phone: +91-9876543210 — High
Card: 4111-1111-1111-1111 — High
IP: 192.168.0.1 — Low


---

📁 Project Structure

pii-detector/
├── logs/              # Input log files
├── output/            # Scanned reports
├── archive/           # Redacted logs (archived)
├── pii-dashboard/     # React dashboard (port 3001)
├── demo.mp4           # Local demo video (optional)
└── log_analyzer.py    # Main scanner


---

🚀 Run the Tool

Scan logs manually:

cd ~/pii-detector
python log_analyzer.py

View Dashboard (port 3001):

cd ~/pii-detector/pii-dashboard
npm install
npm start

Access at: http://localhost:3001


---

⏱️ Schedule Auto Scan (9AM daily)

crontab -e

Paste this:

0 9 * * * cd ~/pii-detector && python log_analyzer.py >> cron_log.txt 2>&1


---

✅ Telegram Alerts

Receive real-time alerts for high-risk detections via Telegram Bot.


---

Made using:

Python (OpenAI API)

React (Chart.js)

Termux on Android

Cron

GitHub

YouTube



---

Connect

Have feedback or want to collaborate?
Ping me on LinkedIn


