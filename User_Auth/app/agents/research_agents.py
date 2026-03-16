import asyncio

from app.tools.web_search import search_web
from app.tools.summerizer import summarize_source
from app.services.llm_service import call_llm


async def generate_report(query, summaries):

    prompt = f"""
    Research Query:
    {query}

    Summaries:
    {summaries}

    Create a structured research report including:

    - Key insights
    - Major trends
    - Conclusion
    """

    return await call_llm(prompt)


async def run_research(query: str):

    sources = await search_web(query)

    summary_tasks = [
        summarize_source(src) for src in sources
    ]

    summaries = await asyncio.gather(*summary_tasks)

    report = await generate_report(query, summaries)

    return {
        "query": query,
        "sources": sources,
        "report": report
    }