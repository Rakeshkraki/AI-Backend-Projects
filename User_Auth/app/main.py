
from fastapi import FastAPI
from app.api.research import router as research_router

app = FastAPI(
    title="Async AI Research Agent",
    version="1.0"
)

app.include_router(research_router)