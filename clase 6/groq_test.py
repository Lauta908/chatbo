import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

import requests

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer TU_API_KEY",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",
    "messages": [{"role": "user", "content": "Hola, ¿quién sos?"}]
}

response = requests.post(url, headers=headers, json=data)

print(response.json()['choices'][0]['message']['content'])


