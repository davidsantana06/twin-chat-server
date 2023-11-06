from os import path


ROOT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__), 
        '..'
    )
)
DATABASE_FOLDER = path.join(ROOT_FOLDER, 'database')
CONVERSATIONS_FOLDER = path.join(DATABASE_FOLDER, 'conversations')
TWIN_CHATTER_DATABASE = path.join(DATABASE_FOLDER, 'twin_chatter.sqlite3')
