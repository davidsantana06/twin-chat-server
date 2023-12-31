from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from .services import get_response


router = APIRouter()


@router.get('/')
def root():
    return RedirectResponse(url='/docs')


@router.get('/response/{statement}')
def response(statement: str):
    return get_response(statement)
