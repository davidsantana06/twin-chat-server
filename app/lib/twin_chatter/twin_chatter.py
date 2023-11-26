from chatterbot import ChatBot
from chatterbot.conversation import Statement
from difflib import SequenceMatcher


class TwinChatter:
    MININUM_CONFIDENCE = .5

    def __init__(self, database_file: str) -> None:
        self.__chat_bot = ChatBot(
            'TwinChatter',
            database_uri=f'sqlite:///{database_file}?check_same_thread=False',
            read_only=True,
            statement_comparison_function=self.compare_statements,
            logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'}]
        )

    @property
    def chat_bot(self) -> ChatBot:
        return self.__chat_bot

    @staticmethod
    def compare_statements(input_statement: Statement, candidate_statement: Statement) -> float:
        confidence = .0
        input_text = input_statement.text
        candidate_text = candidate_statement.text

        if input_text and candidate_text:
            confidence = round(SequenceMatcher(a=input_text, b=candidate_text).ratio(), 2)

        return confidence

    def get_response(self, statement: str) -> str:
        response = self.__chat_bot.get_response(statement.lower())
        return response.text if (response.confidence >= self.MININUM_CONFIDENCE) else 'Não entendi a sua pergunta.'
