from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlmodel import select, SQLModel

from .db import new_session


def is_table_empty(model: SQLModel) -> bool:
    """
    Checks if there are records in the table
    :param model: SQLModel for checking
    :return: check result
    """
    with new_session() as session:
        result = session.exec(select(model).limit(1)).first()
        return result is None


def get_model_objects_with_total_count(model: SQLModel, limit: int, offset: int) -> tuple:
    """
    Returns model objects with total objects count
    :param model: SQLModel from which we receive objects
    :param limit: number of objects to return
    :param offset: number of objects to skip in query
    :return:
    """
    with new_session() as session:
        count = session.exec(select(func.count()).select_from(model)).one()

        query = select(model).offset(offset).limit(limit)
        articles = session.exec(query).all()
        return articles, count


def bulk_insert_into_model(model: SQLModel, data: list[dict]) -> None:
    """
    Bulk data insert into model. Handles duplication by doing nothing on conflict
    :param model: SQLModel in which data inserting
    :param data: data to insert
    :return: None
    """
    with new_session() as session:
        query = pg_insert(model).values(data).on_conflict_do_nothing(index_elements=['url'])
        session.exec(query)
        session.commit()

