from pydantic import BaseModel
from typing import List


class ResearchRequest(BaseModel):
    query: str


class ResearchResponse(BaseModel):
    query: str
    sources: List[str]
    report: str

