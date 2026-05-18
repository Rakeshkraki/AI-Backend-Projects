from fastapi import FastAPI
from pydantic import BaseModel
from app.worker import process_batch

app = FastAPI()


class InferRequest(BaseModel):
    api_key: str
    items: list[str]


@app.post("/infer")
async def infer(payload: InferRequest):
    results = await process_batch(
        payload.items,
        payload.api_key
    )

    return {"results": results}