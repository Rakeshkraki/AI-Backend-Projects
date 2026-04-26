from fastapi import FastAPI
import asyncio
from app.worker import process_batch

app = FastAPI()

app.post("/infer")
async def infer(data : list[str]):
    result = await process_batch(data)
    return {"result" : result}