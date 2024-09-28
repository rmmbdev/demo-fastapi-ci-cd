import asyncio

import asyncpg

from backend.auth_service.app.db.migrations.m_01_setup import migration_queries

MIGRATIONS = [
    *migration_queries,
]


async def migrate():
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/demo')

    # do migrations
    for mig in MIGRATIONS:
        await conn.execute(mig)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(migrate())
