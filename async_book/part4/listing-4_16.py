import asyncio
import aiohttp

from async_book.part4 import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.example.com')
        api_b = fetch_status(session, 'https://www.example.com', delay=2)
        done, pending = await asyncio.wait([api_a, api_b], timeout=1)
        for task in pending:
            if task is api_b:
                print('API B слишком медленный, отмена')
                task.cancel()


asyncio.run(main())
