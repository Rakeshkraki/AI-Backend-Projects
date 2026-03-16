import httpx


async def search_web(query: str):

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json",
        "no_html": 1
    }

    async with httpx.AsyncClient(timeout=30) as client:

        response = await client.get(url, params=params)

        data = response.json()

    results = []

    related = data.get("RelatedTopics", [])

    for item in related[:5]:
        if "Text" in item:
            results.append(item["Text"])

    return results