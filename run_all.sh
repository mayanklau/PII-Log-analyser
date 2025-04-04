#!/data/data/com.termux/files/usr/bin/bash

echo "▶️ Running PII Scan..."
python log_analyzer.py

echo "🔁 Syncing reports to dashboard..."
./sync.sh

echo "🚀 Launching React dashboard..."
cd pii-dashboard
termux-open-url http://localhost:3002
npm start -- --host 0.0.0.0 --port 3002
