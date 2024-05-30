from fastapi import FastAPI
from .database import engine, Base
from .routers import products, users, orders

app = FastAPI()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(products.router)
app.include_router(users.router)
app.include_router(orders.router)