from fastapi import FastAPI, Response

from models import UserLogin


app = FastAPI()


@app.get('/login')
async def login_add_cookie(info: UserLogin, response: Response):
    new_token = '1123qqwe123'
    response.set_cookie(key='session_token', value=new_token)

