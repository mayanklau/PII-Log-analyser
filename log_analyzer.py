import openai
import os

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise Exception("OPENAI_API_KEY is not set")

# Read sample log
with open("sample_logs.txt", "r") as f:
    logs = f.read()

# Send to GPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You're a security analyst. Detect any exposed PII in the following logs. "
                "Use this format:\n- [TYPE]: [VALUE] — [RISK LEVEL]"
            )
        },
        {
            "role": "user",
            "content": logs
        }
    ]
)

# Print GPT response
result = response["choices"][0]["message"]["content"]
print("\nGPT RAW RESPONSE:\n")
print(result)

# Save to file
with open("pii_report_1.md", "w") as f:
    f.write(result)
