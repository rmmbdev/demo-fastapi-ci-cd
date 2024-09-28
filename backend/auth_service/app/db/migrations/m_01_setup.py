_ADD_UUID = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
"""

_CREATE_USERS = """
 CREATE TABLE IF NOT EXISTS users (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hashed VARCHAR(1024) NOT NULL
);
"""

migration_queries = [_ADD_UUID, _CREATE_USERS]
