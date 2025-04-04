import openai
import os
import csv
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise Exception("OpenAI API key not set.")

# Load log file
with open("sample_logs.txt", "r") as file:
    logs = file.read()

# Ask GPT to return structured PII findings only
prompt = (
    "You're a security analyst. Analyze the logs and extract PII. "
    "For each PII item, respond in this strict JSON format:\n"
    "[{\"type\": \"Email\", \"value\": \"john@example.com\", \"risk\": \"Medium\"}, ...]\n"
    "Only return the JSON array. Do not add comments or explanations."
)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": logs}
    ]
)

# Get and parse the JSON string
result_json_str = response["choices"][0]["message"]["content"].strip()

# Save to JSON file
with open("pii_report.json", "w") as jf:
    jf.write(result_json_str)

# Parse JSON into list and write to CSV
try:
    pii_list = json.loads(result_json_str)
    with open("pii_report.csv", "w", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=["type", "value", "risk"])
        writer.writeheader()
        writer.writerows(pii_list)
    print("PII data exported to pii_report.json and pii_report.csv")
except Exception as e:
    print("Error parsing GPT JSON response:", e)
