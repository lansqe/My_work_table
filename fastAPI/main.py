from fastapi import FastAPI
from models import User

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hi all'}


@app.post('/user')
async def users(user: User):
    print({'Name': user.name, 'Id': user.age})


@app.post('/is_adult')
async def adult(user: User):
    is_adult = True if user.age >= 18 else False
    return {
    "name": user.name,
    "age": user.age,
    "is_adult": is_adult
}
