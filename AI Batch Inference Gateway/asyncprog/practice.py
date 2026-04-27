import asyncio
import httpx

async def test():
    async with httpx.AsyncClient() as client:
        tasks = [
            client.post("http://localhost:8000/infer", json=["hello"]*10)
            for _ in range(50)
        ]
        await asyncio.gather(*tasks)

asyncio.run(test())