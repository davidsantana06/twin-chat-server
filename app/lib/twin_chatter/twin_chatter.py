from chatterbot import ChatBot
from chatterbot.conversation import Statement
from difflib import SequenceMatcher
from typing import Union

from app.constants import TWIN_CHATTER_DATABASE


class TwinChatter:
    MININUM_CONFIDENCE = .5

    def __init__(self) -> None:
        self.chat_bot = ChatBot(
            'TwinChat',
            database_uri=f'sqlite:///{TWIN_CHATTER_DATABASE}',
            read_only=True,
            statement_comparison_function=self.compare_messages,
            logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'}]
        )

    @staticmethod
    def compare_messages(input_message: Statement, candidate_message: Statement) -> float:
        confidence = .0
        input_text = input_message.text
        candidate_text = candidate_message.text

        if input_text and candidate_text:
            confidence = SequenceMatcher(None, input_text, candidate_text)
            confidence = round(confidence.ratio(), 2)

        return confidence

    def get_response(self, question: str) -> Union[None, str]:
        response = self.chat_bot.get_response(question.lower())
        return response.text if (response.confidence >= self.MININUM_CONFIDENCE) else None