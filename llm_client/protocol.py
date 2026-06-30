from typing import Protocol, List
from llm_client.schema import Message, ModelResponse

class LLMClient(Protocol):
    def chat(self, model:str, messages:List[Message]) -> ModelResponse:
        ...