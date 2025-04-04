import openai
import os
import csv
import json
from datetime import datetime
import subprocess

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise Exception("OPENAI_API_KEY is not set.")

# Define folders
logs_folder = "logs"
output_folder = "output"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to process a single log file
def process_log_file(log_file_path, output_prefix):
    with open(log_file_path, "r") as file:
        logs = file.read()

    # --- Part 1: Get PII detection and redacted logs in a combined response ---
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a security analyst. From the logs below:\n"
                    "1. Extract exposed PII items and label them with risk levels (High/Medium/Low).\n"
                    "2. Create a redacted version of the log where PII is masked.\n"
                    "Output as two sections:\n"
                    "### PII Detection\n"
                    "- [TYPE]: [VALUE] — [RISK LEVEL]\n\n"
                    "### Redacted Logs\n"
                    "[Redacted log content here]"
                )
            },
            {"role": "user", "content": logs}
        ]
    )

    result = response["choices"][0]["message"]["content"]

    # Save combined report (Markdown)
    md_file = os.path.join(output_folder, f"{output_prefix}_report.md")
    with open(md_file, "w") as f:
        f.write(result)

    # --- Part 2: Get structured JSON output for CSV/JSON exports ---
    json_prompt = (
        "You are a security analyst. Analyze the following log and extract any exposed PII. "
        "For each PII item, output a JSON array with objects that have keys: 'type', 'value', 'risk'. "
        "For example: "
        '[{"type": "Email", "value": "john@example.com", "risk": "Medium"}, ...]. '
        "Only return the JSON array."
    )

    response_json = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": json_prompt},
            {"role": "user", "content": logs}
        ]
    )

    result_json_str = response_json["choices"][0]["message"]["content"].strip()

    # Save JSON report
    json_file = os.path.join(output_folder, f"{output_prefix}_report.json")
    with open(json_file, "w") as jf:
        jf.write(result_json_str)

    # Parse JSON and export to CSV
    try:
        pii_list = json.loads(result_json_str)
        csv_file = os.path.join(output_folder, f"{output_prefix}_report.csv")
        with open(csv_file, "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=["type", "value", "risk"])
            writer.writeheader()
            writer.writerows(pii_list)
    except Exception as e:
        print("Error parsing JSON for", log_file_path, ":", e)

    print(f"Processed {log_file_path}. Reports saved to output folder.")

# Loop through all files in the logs folder
for filename in os.listdir(logs_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(logs_folder, filename)
        # Use the file name (without extension) as output prefix
        prefix = os.path.splitext(filename)[0]
        process_log_file(file_path, prefix)

# --- Optional: Auto GitHub Push after processing batch ---
now = datetime.now().strftime("%Y-%m-%d %H:%M")
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Auto: Batch PII scan and export - {now}"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Batch reports pushed to GitHub.")
except Exception as e:
    print("Git push failed:", e)
