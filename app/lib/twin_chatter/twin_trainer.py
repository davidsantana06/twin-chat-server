from chatterbot.trainers import ListTrainer
from os import (
    path,
    listdir
)
from typing import Dict, List
import json

from app.constants import CONVERSATIONS_FOLDER

from .twin_chatter import TwinChatter


class TwinTrainer:
    def __init__(self, twin_chatter: TwinChatter) -> None:
        self.list_trainer = ListTrainer(
            twin_chatter.chat_bot
        )
        self.conversations = self.import_conversations()

    @staticmethod
    def import_conversations() -> List[List[Dict[str, object]]]:
        conversations = []

        for file in listdir(CONVERSATIONS_FOLDER):
            conversation_file = path.join(CONVERSATIONS_FOLDER, file)

            with open(conversation_file, 'r', encoding='utf-8') as conversation:
                conversations.append(
                    json.load(conversation)
                )

        return conversations
    
    def train(self) -> None:
        for conversation in self.conversations:
            for entry in conversation:
                statements = entry.get('statements')
                response = entry.get('response')

                for statement in statements:
                    self.list_trainer.train([statement, response])
