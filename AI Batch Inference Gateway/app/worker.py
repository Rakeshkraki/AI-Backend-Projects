
import asyncio
from app.rate_limiter import RateLimiter

CONCURRENCY_LIMIT = 100
semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
rate_limiter = RateLimiter(rate_per_sec=5)


async def fake_inference(text: str):
    await asyncio.sleep(1)  # simulate model/API
    return text.upper()

async def process_item(item, api_key):
    await rate_limiter.acquire(api_key)

    async with semaphore:
        return await fake_inference(item)

async def process_batch(items):
    results = []

    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(process_item(i)) for i in items]

    for t in tasks:
        results.append(t.result())

    return results