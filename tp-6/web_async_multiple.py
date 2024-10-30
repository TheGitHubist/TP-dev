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
    tasks = [get_content(url) for url in url_list]
    contents = await asyncio.gather(*tasks)
    for url, content in zip(url_list, contents):
        print(f"Content for {url} fetched.")
        file_name = '/tmp/web_' + url.split("/")[-1]
        asyncio.run(write_content(content, file_name))
        print(f"Content saved to /tmp/web_{file_name}.")

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))