from pydantic import BaseModel, ConfigDict, Field, computed_field
from typing import Literal

class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"] = Field(..., description="Role of the message author")
    content: str = Field(..., description="Textual content of the message")

class TokenUsage(BaseModel):
    prompt_tokens: int = Field(..., description="Number of tokens in the input prompt")
    completion_tokens: int = Field(..., description="Number of tokens in generated completion")

    @computed_field
    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens

class ModelResponse(BaseModel):
    model_config = ConfigDict(frozen=True)
    content: str = Field(..., description="Generated text answer from the model")
    model: str = Field(..., description="Specific model used for answer generation")
    usage: TokenUsage = Field(..., description="Token breakdown statistics for the execution")
    finish_reason: str = Field(..., description="Termination signal")
    latency_ms: float = Field(..., description="Total roundtrip API execution duration in ms")