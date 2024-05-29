from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База данных очищена")
    await create_tables()
    print("База данных готова к работе")
    yield
    print("Выключение приложения")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)