from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    id: int
    title: str
    content: str
    author: str
    url: str
    published_at: datetime
    scraped_at: datetime
    subtitle: Optional[str] = None
    image_url: Optional[str] = None
    word_count: Optional[int] = None
    reading_time: Optional[str] = None


class ArticleListSchema(BaseModel):
    total_count: int
    items: List[ArticleSchema]
