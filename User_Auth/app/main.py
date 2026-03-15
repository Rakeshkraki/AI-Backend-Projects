from fastapi import FastAPI

app = FastAPI()

async def research(query: str):
    result = await run_research(query)
    return result