from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool


class UserLogin(BaseModel):
    login: str
    password: str | int

