import aiofiles
import aiohttp
import asyncio
import sys

async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def write_content(content, file):
    async with aiofiles.open(file, 'w') as f:
        await f.write(content)

async def main(url_list):
    tasks = [write_content(await get_content(url), '/tmp/web_' + url.split("/")[-1]) for url in url_list]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))