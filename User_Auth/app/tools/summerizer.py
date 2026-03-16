from app.services.llm_service import call_llm
from app.utils.async_utils import limited_async_call


async def summarize_source(source: str):

    prompt = f"""
    Summarize the following research content:

    {source}

    Provide a short informative summary.
    """

    summary = await limited_async_call(call_llm(prompt))

    return summary