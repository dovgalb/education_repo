import asyncio


async def delay(delay_seconds: (int, float)) -> float:
    print(f'{40 * "-"}\n'
          f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return '-' * 10, delay_seconds
