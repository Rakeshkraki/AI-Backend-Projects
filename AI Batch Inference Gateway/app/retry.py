# app/retry.py
import asyncio

async def retry(coro, retries=3, delay=1):
    for attempt in range(retries):
        try:
            return await coro()
        except Exception as e:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(delay * (2 ** attempt))  # exponential backoff
    return None