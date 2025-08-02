from datetime import datetime

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, ARRAY, String
from typing import Optional, List

# TODO: add related articles and tags later


class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(unique=True)
    title: str
    content: str
    author: str
    published_at: datetime
    scraped_at: datetime
    subtitle: Optional[str] = Field(default=None)
    image_url: Optional[str] = Field(default=None)
    word_count: Optional[int] = Field(default=None)
    reading_time: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(String())))
    related_articles: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(String())))
