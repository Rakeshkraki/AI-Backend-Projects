from fastapi import APIRouter
from app.models.schemas import ResearchRequest, ResearchResponse
from app.agents.research_agent import run_research

router = APIRouter(prefix="/research", tags=["Research"])


@router.post("/", response_model=ResearchResponse)
async def research_endpoint(request: ResearchRequest):

    result = await run_research(request.query)

    return result