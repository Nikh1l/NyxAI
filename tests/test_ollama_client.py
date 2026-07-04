import unittest
from core.ollama.client import OllamaClient

class TestOllamaClient(unittest.TestCase):
    def test_generate(self):
        client = OllamaClient()
        response = client.generate(model="qwen3:30b-a3b", prompt="Hello NyxAI!", stream=False)
        self.assertIn("response", response)
        self.assertIsInstance(response["response"], str)

    def test_chat(self):
        client = OllamaClient()
        messages = [
            {"role": "user", "content": "What is the capital of France?"}
        ]
        response = client.chat(model="qwen3:30b-a3b", messages=messages, stream=False)
        self.assertIn("message", response)
        self.assertIn("content", response["message"])
        self.assertIsInstance(response["message"]["content"], str)

if __name__ == '__main__':
    unittest.main()