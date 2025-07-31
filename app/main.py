from fastapi import FastAPI
from database.db import init_db


def get_application() -> FastAPI:
    application = FastAPI()
    init_db()

    @application.get('/')
    async def root():
        return {'message': 'hello'}

    return application


app = get_application()
