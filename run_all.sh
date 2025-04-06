#!/data/data/com.termux/files/usr/bin/bash

echo "▶️ Running PII Scan..."
python log_analyzer.py

echo "📊 Starting React Dashboard..."
cd pii-dashboard

# Check if already running
if ! pgrep -f "react-scripts start" > /dev/null; then
  termux-open-url http://localhost:3002
  nohup npm start -- --host 0.0.0.0 --port 3002 > dashboard.log 2>&1 &
  echo "✅ Dashboard started in background"
else
  echo "ℹ️ Dashboard is already running"
fi
