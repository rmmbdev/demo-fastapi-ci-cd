_ADD_UUID = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
"""

_CREATE_DOCS = """
CREATE TABLE IF NOT EXISTS docs (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    content TEXT
);
"""



migration_queries = [_ADD_UUID, _CREATE_DOCS]
