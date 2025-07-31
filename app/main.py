from fastapi import FastAPI
from database.db import init_db
from api.router import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router, prefix='/api/v1')
    init_db()

    @application.get('/')
    async def root():
        return {'message': 'hello'}

    return application


app = get_application()
