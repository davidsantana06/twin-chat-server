from dotenv import load_dotenv
from fastapi import FastAPI
from os import path

from .constants import ROOT_FOLDER
from .routes import router


def create_app() -> FastAPI:
    load_dotenv(
        path.join(ROOT_FOLDER, '.env')
    )

    app = FastAPI(
        title='TwinChat API',
        description=(
            'The TwinChat is a straightforward platform for providing ' + \
            'answers to fitness-related questions in Portuguese (PT-BR).'
        ),
        version='0.1.0'
    )
    app.include_router(router)

    return app
