from typing import Dict, Any
from llm_client.schema import ModelResponse, TokenUsage

def from_ollama(raw:Dict[str, Any], latency_ms:float) -> ModelResponse:
    return ModelResponse(
        content=raw["message"]["content"],
        model=raw["model"],
        finish_reason=raw.get("done_reason", "stop"),
        usage= TokenUsage(
            prompt_tokens=raw.get("prompt_eval_count", 0),
            completion_tokens=raw.get("eval_count", 0)),
        latency_ms=latency_ms,
    )