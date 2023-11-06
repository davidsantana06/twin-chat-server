from app.lib.twin_chatter import TwinChatter


twin_chatter = TwinChatter()


def get_response(statement: str):
    return twin_chatter.get_response(statement)
