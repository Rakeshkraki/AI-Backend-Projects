async def generate_report(query, summaries):

    prompt = f"""
    Research query: {query}

    Summaries:
    {summaries}

    Generate a detailed research report.
    """

    return await call_llm(prompt)