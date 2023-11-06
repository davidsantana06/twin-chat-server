from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from .services import get_response


router = APIRouter()


@router.get('/')
def index():
    return RedirectResponse(url='/docs')


@router.get('/response/{message}')
def response(message: str):
    return {'response': get_response(message)}
