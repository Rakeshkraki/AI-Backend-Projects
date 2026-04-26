import asyncio

async def task(n):
    await asyncio.sleep(n)
    return n

async def main():
    tasks = [task(1), task(2)]
    done, pending = await asyncio.wait(tasks)

    for d in done:
        print(d.result())

asyncio.run(main())