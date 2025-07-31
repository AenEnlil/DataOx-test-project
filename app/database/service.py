from typing import Type

from sqlalchemy import func
from sqlmodel import select, SQLModel

from .db import new_session


def is_table_empty(model: Type) -> bool:
    with new_session() as session:
        result = session.exec(select(model).limit(1)).first()
        return result is None


def get_model_objects_with_total_count(model: SQLModel, limit: int, offset: int) -> tuple:
    with new_session() as session:
        count = session.exec(select(func.count()).select_from(model)).one()

        query = select(model).offset(offset).limit(limit)
        articles = session.exec(query).all()
        return articles, count
