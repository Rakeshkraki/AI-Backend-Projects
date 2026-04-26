# Async IO, event loop, Coroutines vs threads

import asyncio


async def fetch_data(delay, id):
    print("Start Data Fetching.........", id)
    await asyncio.sleep(delay)
    print("Data fetched", id)

    return {"data": "Hello", "id": id}


async def main():
    print("Start of main coroutines")
    task = fetch_data(4,1)
    print("End of main coroutines")
    result = await task

    print(result)


# main()
asyncio.run(main())
