import openai
import os
import json
import csv
import requests
from datetime import datetime

# Set your OpenAI API Key from env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Telegram Bot Config
TELEGRAM_BOT_TOKEN = "7934281490:AAEHF4MRC5xX7tjY72-c4bqIOuW-x_kenAA"
TELEGRAM_CHAT_ID = "215046961"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram alert failed:", e)

logs_folder = "logs"
output_folder = "output"
archive_folder = "archive"
os.makedirs(output_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

for filename in os.listdir(logs_folder):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(logs_folder, filename)
    prefix = os.path.splitext(filename)[0]

    with open(file_path, "r") as file:
        logs = file.read()

    # Step 1: GPT PII Detection
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Detect PII, assign High/Medium/Low risk, and redact sensitive data."},
            {"role": "user", "content": logs}
        ]
    )["choices"][0]["message"]["content"]

    with open(f"{output_folder}/{prefix}_report.md", "w") as f:
        f.write(result)

    # Step 2: GPT JSON Output
    json_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Return only JSON array of PII with keys: type, value, risk."},
            {"role": "user", "content": logs}
        ]
    )["choices"][0]["message"]["content"]

    with open(f"{output_folder}/{prefix}_report.json", "w") as jf:
        jf.write(json_response)

    # Step 3: CSV Export
    try:
        pii_list = json.loads(json_response)
        with open(f"{output_folder}/{prefix}_report.csv", "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=["type", "value", "risk"])
            writer.writeheader()
            writer.writerows(pii_list)
    except Exception as e:
        print("CSV Error:", e)
        pii_list = []

    # Step 4: Telegram Alert if High Risk
    high_risk_items = [item for item in pii_list if item["risk"].lower() == "high"]
    if high_risk_items:
        alert_msg = f"⚠️ High-risk PII found in `{filename}`:\n"
        for item in high_risk_items:
            alert_msg += f"- {item['type']}: {item['value']}\n"
        send_telegram_alert(alert_msg)

    # Step 5: Archive Log After Scan
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    archive_filename = f"{prefix}_{timestamp}.txt"
    os.rename(file_path, os.path.join(archive_folder, archive_filename))

    print(f"Processed {filename} — reports saved, archived, and alerts sent if needed.")

# Step 6: Weekly ZIP (force now for testing)
if True:
    zip_name = f"archive_backup_{datetime.now().strftime('%Y%m%d')}.zip"
    os.system(f"cd archive && zip -r {zip_name} *.txt && rm *.txt")
    print(f"Archived logs zipped as {zip_name}")

# Auto Git Push
now = datetime.now().strftime("%Y-%m-%d %H:%M")
os.system("git add .")
os.system(f"git commit -m 'Auto: Full pipeline + Telegram + Archive + Weekly ZIP - {now}'")
os.system("git push")
