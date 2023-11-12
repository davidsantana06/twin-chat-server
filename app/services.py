from app.constants import TWIN_CHATTER_DATABASE
from app.lib.twin_chatter import TwinChatter


twin_chatter = TwinChatter(TWIN_CHATTER_DATABASE)


def get_response(statement: str):
    return twin_chatter.get_response(statement)
