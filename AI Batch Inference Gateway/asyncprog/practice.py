# Async IO, event loop, Coroutines vs threads

import asyncio


async def fetch_data(delay, ids):
    print("Start Data Fetching.........", ids)
    await asyncio.sleep(delay)
    print("Data fetched", ids)

    return {"data": "Hello", "id": ids}


async def main():
    print("Start of main coroutines")
    # task = asyncio.create_task(fetch_data(5,1))
    # task2 =asyncio.create_task(fetch_data(2, 2))

    task = asyncio.gather(fetch_data(1,1), fetch_data(2,2))
    print("End of main coroutines")

    result = await task
    print(result)

    # result2 = await task2
    # print(result2)


# main()
asyncio.run(main())
