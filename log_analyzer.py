import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise Exception("OpenAI key not found. Please set OPENAI_API_KEY in your environment.")

# Load log file
with open("sample_logs.txt", "r") as file:
    logs = file.read()

# Chunk logs to avoid token limit
chunks = [logs[i:i+1500] for i in range(0, len(logs), 1500)]

for i, chunk in enumerate(chunks):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a security expert. Identify possible PII leaks (names, emails, IPs, phone numbers, card numbers, etc) in the logs below."},
            {"role": "user", "content": chunk}
        ]
    )

    result = response['choices'][0]['message']['content']
    
    with open(f"pii_report_{i+1}.md", "w") as f:
        f.write(result)

print("Analysis complete. Reports saved as .md files.")
