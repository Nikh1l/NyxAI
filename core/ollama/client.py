import requests
import json

class OllamaClient:

    def __init__(self, host="http://localhost:11434"):
        self.host = host

    def generate(self, model, prompt, stream=False):
        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": stream,
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["response"]
    

    def chat(self, model, messages, stream=False):
        response = requests.post(
            f"{self.host}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": stream,
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]
    
    def stream_chat(self, model, messages):
        with requests.post(
            f"{self.host}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": True,
            },
            stream=True
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line:
                    continue
                yield json.loads(line)