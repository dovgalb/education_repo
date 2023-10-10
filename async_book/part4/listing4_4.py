import asyncio
import aiohttp
from async_book.four_part import fetch_status
from async_book.util.async_timer import async_timed
from async_book.util.delay_functions import delay


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://www.vk.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.run(main())