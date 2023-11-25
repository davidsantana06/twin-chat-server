from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import path

from .constants import ROOT_FOLDER
from .routes import router


def create_app() -> FastAPI:
    load_dotenv(path.join(ROOT_FOLDER, '.env'))

    app = FastAPI(
        title='TwinChat API',
        description='TwinChat is a straightforward platform for providing answers to fitness-related questions in Portuguese (PT-BR).',
        version='0.1.0'
    )
    app.add_middleware(CORSMiddleware, allow_origins=['*'])
    app.include_router(router)

    return app
