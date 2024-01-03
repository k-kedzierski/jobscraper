import functools
import random
from typing import Dict


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
]

@functools.lru_cache(maxsize=1)
def get_default_headers() -> Dict[str, str]:
    return {"user-agent": random.choice(USER_AGENTS)}