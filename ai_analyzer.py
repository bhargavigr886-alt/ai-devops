import os
import requests
import json

# Get keys from GitHub Secrets
groq_api_key = os.environ.get("GROQ_API_KEY")
discord_webhook = os.environ.get("DISCORD_WEBHOOK_URL")

# A sample error log from our failed test
error_log = """
============================= test session starts ==============================
collected 3 items
test_app.py ..F                                                          [100%]
=================================== FAILURES ===================================
________________________________ test_divide_by_zero ___________________________
    def test_divide_by_zero():
>       assert divide_numbers(10, 0) == 0
E       ZeroDivisionError: division by zero
=========================== short test summary info ============================
FAILED test_app.py::test_divide_by_zero - ZeroDivisionError: division by zero
"""

print("Sending logs to AI (Groq)...")
# 1. Ask the AI (Groq)
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "llama3-8b-8192",
    "messages": [
        {"role": "system", "content": "You are a Senior DevOps Engineer. Analyze this error log and explain how to fix it in 2 short sentences."},
        {"role": "user", "content": error_log}
    ]
}

response = requests.post(url, headers=headers, json=data)
ai_response = response.json()['choices'][0]['message']['content']
print("AI Response received!")

# 2. Send to Discord
print("Sending AI analysis to Discord...")
discord_data = {
    "content": f"🚨 **Pipeline Failed!**\n\n**AI Analysis:**\n{ai_response}"
}
requests.post(discord_webhook, json=discord_data)
print("Message sent to Discord successfully!")
