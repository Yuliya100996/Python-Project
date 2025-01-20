from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get('/')
async def input() -> str:
    return (f'Главная страница')


@app.get('/user/admin')
async def welcome() -> str:
    return (f'Вы вошли как администратор')


@app.get('/user/{user_id}')
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID',example=11)]):
    return (f'Вы вошли как пользователь № {user_id}')


@app.get('/user/{username}/{age}')
async def user_inf(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Yuliya')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=28)]):
    return (f'Информация о пользователе. Имя: {username}, Возраст: {age}')
