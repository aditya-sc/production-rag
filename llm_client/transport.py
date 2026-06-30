import time
import requests
from typing import Any, Dict

def timed_post(url:str, payload:Dict[str, Any], timeout:float=60) -> tuple[requests.Response, float]:
    start = time.perf_counter()
    response = requests.post(url, json=payload, timeout=timeout)
    latency_ms = (time.perf_counter() - start) * 1000
    return response, latency_ms