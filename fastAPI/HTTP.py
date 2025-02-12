from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hi all'}


@app.post('/calculate')
async def root(num1: int, num2: int):
    return {'message': num1 + num2}

