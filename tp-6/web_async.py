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

async def main(url, output_file):
    try:
        content = await get_content(url)
        await write_content(content, output_file)
        print(f"Downloaded content from {url} and saved it to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":    
    url = sys.argv[1]
    output_file = '/tmp/web_page_async'
    asyncio.run(main(url, output_file))