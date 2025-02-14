from fastapi import FastAPI
from models import User, Feedback

app = FastAPI()
data_feedback = []

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


@app.post('/feedback')
async def users_feedback(f: Feedback):
    data_feedback.append({'name': f.name, 'comments': f.message})
    return {
        'message': f"Feedback received. Thank you, {f.name}!"
    }


@app.get('/comments')
async def show_feedback():
    return data_feedback

