from os import environ
import uvicorn

from app import create_app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(
        app, host=environ.get('HOST'), port=int(environ.get('PORT'))
    )
