from database.models.article import Article
from database.service import get_model_objects_with_total_count


def get_articles_list(limit: int, offset: int) -> dict:
    articles, count = get_model_objects_with_total_count(Article, limit=limit, offset=offset)
    return {'total_count': count, 'items': articles}
