import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5436,
                                       user='postgres',
                                       database='postgres',
                                       password='password')

    statements = [CREATE_BRAND_TABLE,
                  REATE_PRODUCT_TABLE,
                  REATE_PRODUCT_COLOR_TABLE,
                  REATE_PRODUCT_SIZE_TABLE,
                  REATE_SKU_TABLE,
                  IZE_INSERT,
                  OLOR_INSERT]

    print('Создается база данных product...')

    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана!')
    await connection.close()

asyncio.run(main())
