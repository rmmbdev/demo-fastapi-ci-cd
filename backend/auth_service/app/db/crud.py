import asyncpg

from backend.auth_service.app.api.schemas import RegisterInput, UserBase
from backend.auth_service.app.api.utils import get_password_hash


async def create_user(*, user_create: RegisterInput) -> UserBase:
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:postgres@localhost:5432/demo')

    db_user = UserBase(email=user_create.email,
                       password_hashed=get_password_hash(user_create.password))

    await conn.execute(
        '''
        INSERT INTO users (email,password_hashed) values ($1,$2)
        ''', db_user.email, db_user.password_hashed
    )

    await conn.close()

    return db_user
