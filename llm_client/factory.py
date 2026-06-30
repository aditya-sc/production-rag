from typing import Dict, Type

from llm_client.protocol import LLMClient
from llm_client.providers import OllamaClient

class LLMClientFactory:
    _registry: Dict[str, Type] = {
        "ollama": OllamaClient
    }

    @classmethod
    def get_client(cls, provider:str) -> LLMClient: 
        provider_key = provider.lower()
        client_class = cls._registry.get(provider_key)

        if not client_class:
            raise ValueError(f"Unsupported provider '{provider}'. "
                             f"Supported providers are: {list(cls._registry.keys())}")

        return client_class()
        