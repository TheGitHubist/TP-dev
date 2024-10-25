import time
import asyncio

async def count():
    for i in range(10):
        print(i)
        time.sleep(0.5)

async def main():
    tasks = [count(), count()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
