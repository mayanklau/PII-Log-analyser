log_analyzer.py

import os import re import json import csv from datetime import datetime import subprocess

--- Setup ---

log_folder = os.path.expanduser("/pii-detector/output") archive_folder = os.path.expanduser("~/pii-detector/archive") os.makedirs(output_folder, exist_ok=True) os.makedirs(archive_folder, exist_ok=True)

--- PII Patterns ---

patterns = { "Email": (r"[\w.-]+@[\w.-]+", "Medium"), "Phone": (r"+?\d{1,3}[-.\s]?\d{10}", "High"), "Card": (r"\b(?:\d[ -]*?){13,16}\b", "High"), "IP": (r"\b(?:\d{1,3}.){3}\d{1,3}\b", "Low") }

--- Scan and Generate Reports ---

for filename in os.listdir(log_folder): if filename.endswith(".txt"): filepath = os.path.join(log_folder, filename) with open(filepath, "r") as file: content = file.read()

findings = []
    redacted = content

    for pii_type, (regex, risk) in patterns.items():
        matches = re.findall(regex, content)
        for match in matches:
            findings.append({"type": pii_type, "value": match, "risk": risk})
            redacted = redacted.replace(match, "[REDACTED]")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    base = os.path.splitext(filename)[0]
    json_path = os.path.join(output_folder, f"{base}_report.json")
    csv_path = os.path.join(output_folder, f"{base}_report.csv")
    md_path = os.path.join(output_folder, f"{base}_report.md")
    archive_name = os.path.join(archive_folder, f"{base}_{timestamp}.txt")

    with open(json_path, "w") as f:
        json.dump(findings, f)

    with open(csv_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["type", "value", "risk"])
        writer.writeheader()
        writer.writerows(findings)

    with open(md_path, "w") as f:
        f.write("### PII Detection\n")
        for item in findings:
            f.write(f"- {item['type']}: {item['value']} — {item['risk']}\n")
        f.write("\n### Redacted Logs\n")
        f.write(redacted)

    os.rename(filepath, archive_name)
    print(f"Processed {filename}. Reports saved to output folder.")

--- Auto Sync JSON to Dashboard ---

print("\n🔁 Syncing reports to React dashboard...") subprocess.run(["bash", "sync.sh"])

--- Auto Open Dashboard in Browser ---

print("🚀 Opening dashboard in browser...") subprocess.run(["termux-open-url", "http://localhost:3002"])

--- Weekly Archive Cleanup (Sunday) ---

if datetime.now().strftime("%A") == "Sunday": print("🗂 Archiving scanned logs for weekly backup...") zip_filename = os.path.join(archive_folder, f"archive_backup_{datetime.now().strftime('%Y%m%d')}.zip") os.system(f"cd {archive_folder} && zip {zip_filename} *.txt && rm *.txt") print("✅ Archived and cleaned old logs.")

