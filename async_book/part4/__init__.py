import asyncio

from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, delay=0) -> int:
    async with session.get(url) as result:
        await asyncio.sleep(delay)
        print(result.status)
        return result.status