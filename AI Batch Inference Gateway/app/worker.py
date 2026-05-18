import asyncio
from app.rate_limiter import RateLimiter
from app.shutdown import shutdown_event
from app.retry import retry

CONCURRENCY_LIMIT = 5

semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
rate_limiter = RateLimiter(rate_per_sec=8)


async def fake_inference(text: str):
    await asyncio.sleep(1)
    return text.upper()


async def process_item(item: str, api_key: str):
    async def task():
        await rate_limiter.acquire(api_key)

        async with semaphore:
            return await asyncio.wait_for(
                fake_inference(item),
                timeout=10
            )

    try:
        return await retry(task)
    except Exception as e:
        return {"error": str(e), "item": item}


async def process_batch(items: list[str], api_key: str):
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for item in items:
            if shutdown_event.is_set():
                break

            tasks.append(
                tg.create_task(process_item(item, api_key))
            )

    return [t.result() for t in tasks]