from sqlalchemy.util.concurrency import asyncio

from app.tools.summerize import summarize_article
from app.tools.web_search import search_web

async def run_research(query: str):
    sources = await search_web(query)
    summaries = await asyncio.gather(
        *[summarize_article(src) for src in sources]
    )
    final_report = await generate_report(query, summaries)
    return final_report