import asyncio
import aiohttp
from async_book.util.delay_functions import delay
from async_book.util import async_timed
from async_book.four_part import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com', 'python://example.com', 'https://example.com', 'https://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*tasks, return_exceptions=True)
        print(status_codes)

asyncio.run(main())