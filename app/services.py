from app.lib.twin_chatter import TwinChatter


twin_chatter = TwinChatter()


def get_response(message: str):
    return twin_chatter.get_response(message)
