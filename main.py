import asyncio

from boat_loan_bot.surrealdb.clients import HTTPClient

sdb = HTTPClient(
    'http://localhost:8000',
    namespace="test",
    database="test",
    username="root",
    password="root",
)


async def add_boat(name, price, max_speed):
    response = await sdb.create_one(
        'boat',
        name,
        {
            'price': price,
            'max_speed': max_speed,
        }
    )
    print(response)


async def get_all_boats():
    table = 'boat'
    response = await sdb.select_all(table)
    print(response)


async def run_all():
    await add_boat('', 55000.00, 300)
    await get_all_boats()

if __name__ == '__main__':
    asyncio.run(run_all())
