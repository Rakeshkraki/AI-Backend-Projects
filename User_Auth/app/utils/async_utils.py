import asyncio
from app.config import settings

llm_semaphore = asyncio.Semaphore(settings.MAX_CONCURRENT_LLM_CALLS)


async def limited_async_call(coro):

    async with llm_semaphore:
        return await coro