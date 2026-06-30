import requests
from typing import List
from llm_client.parsers import from_ollama
from llm_client.schema import Message, ModelResponse
from llm_client.transport import timed_post


class OllamaClient:
    def __init__(self, url="http://localhost:11434/api/chat"):
        self.url = url

    def chat(self, model:str, messages:List[Message]) -> ModelResponse:
        payload = {
            "model": model,
            "messages": [m.model_dump() for m in messages],
            "stream": False
        }
        response, latency_ms = timed_post(self.url, payload=payload)
        response.raise_for_status()
        return from_ollama(response.json(), latency_ms)
