from typing import Type
from sqlmodel import select

from .db import new_session


def is_table_empty(model: Type) -> bool:
    with new_session() as session:
        result = session.exec(select(model).limit(1)).first()
        return result is None
