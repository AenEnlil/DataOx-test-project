from fastapi import Query
from fastapi.routing import APIRouter
from starlette import status

from .service import get_articles_list
from .schemas import ArticleListSchema

router = APIRouter(prefix='/articles')


@router.get('/', status_code=status.HTTP_200_OK, name='articles:list', response_model=ArticleListSchema)
async def articles_list(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    return get_articles_list(limit=limit, offset=offset)

