from sqlmodel import create_engine, Session, SQLModel
from settings.base import get_settings
from .models import *


def get_connection_string() -> str:
    settings = get_settings()
    user, password = settings.DATABASE_USER, settings.DATABASE_PASSWORD
    db_host, db_port, db_name = settings.DATABASE_HOST, settings.DATABASE_PORT, settings.DATABASE_NAME
    return f'postgresql://{user}:{password}@{db_host}:{db_port}/{db_name}'


engine = create_engine(get_connection_string())


def init_db():
    SQLModel.metadata.create_all(engine)


def new_session() -> Session:
    return Session(engine)


