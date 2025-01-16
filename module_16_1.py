from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def get_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user(user_id: str) -> str:
    return "Вы вошли как пользователь № " + user_id

@app.get("/user")
async def get_user_data(username: str, age: str) -> str:
    return f"Информация о пользователе. Имя: '{username}', Возраст: {age}."
