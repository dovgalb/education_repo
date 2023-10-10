import asyncpg
import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5436,
                                       user='postgres',
                                       database='products',
                                       password='password')

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(60)
        for product in products:
            print(product)
    await connection.close()


asyncio.run(main())
