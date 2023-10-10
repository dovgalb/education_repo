import asyncio
import logging

import aiohttp
from aiohttp import ClientSession

from async_book.util import async_timed


async def fetch_status(session: ClientSession,
                       url: str,
                       delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:

        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.example.com')),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com')),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)
        
        for pending_task in pending:
            pending_task.cancel()





asyncio.run(main())

