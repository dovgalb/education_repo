import asyncio
import aiohttp
from aiohttp import ClientSession
from async_book.util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=5, connect=1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://www.vk.com')

asyncio.run(main())
