# pydantic models
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password_hashed: str


class RegisterInput(BaseModel):
    email: EmailStr
    password: str
