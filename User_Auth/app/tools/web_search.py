import httpx

async def search_web(query: str):

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://api.duckduckgo.com",
            params={"q": query, "format": "json"}
        )

    return response.json()