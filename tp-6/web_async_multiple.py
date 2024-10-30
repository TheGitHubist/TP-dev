import aiofiles
import aiohttp
import asyncio
import sys
import os

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except aiohttp.ClientError:
        return ''

async def write_content(content, file, url):
    try:
        async with aiofiles.open(file, 'w') as f:
            await f.write(content)
        print(f'Content of {url} written to /tmp/web_async_{os.path.basename(url)}')
    except Exception as e:
        print(f'Error writing content to file: {str(e)}')

async def main(url_list_file):
    urls = []
    with open(url_list_file, 'r') as f:
        for line in f:
            urls.append(line.strip())
    tasks = [write_content(await get_content(url), '/tmp/web_async_' + os.path.basename(url), url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))