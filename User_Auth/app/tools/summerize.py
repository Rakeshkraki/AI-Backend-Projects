async def summarize_article(text: str):

    response = await openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize: {text}"}
        ]
    )

    return response.choices[0].message.content