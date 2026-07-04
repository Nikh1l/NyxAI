import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen3:30b-a3b",
    "prompt": "Hello NyxAI!",
    "stream": False,
}

response = requests.post(url, json=payload)
print(response.text)