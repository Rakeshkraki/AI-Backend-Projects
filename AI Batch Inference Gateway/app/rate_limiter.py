# app/rate_limiter.py
import asyncio
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, rate_per_sec: int):
        self.rate = rate_per_sec
        self.tokens = defaultdict(lambda: rate_per_sec)
        self.last_updated = defaultdict(time.time)
        self.lock = asyncio.Lock()

    async def acquire(self, key: str):
        async with self.lock:
            now = time.time()
            elapsed = now - self.last_updated[key]

            # refill tokens
            self.tokens[key] = min(
                self.rate,
                self.tokens[key] + elapsed * self.rate
            )

            if self.tokens[key] < 1:
                await asyncio.sleep(1 / self.rate)

            self.tokens[key] -= 1
            self.last_updated[key] = now