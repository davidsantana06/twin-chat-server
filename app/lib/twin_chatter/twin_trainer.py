from chatterbot.trainers import ListTrainer
from os import (
    path,
    listdir
)
from typing import Dict, List
import json

from .twin_chatter import TwinChatter


class TwinTrainer:
    def __init__(self, twin_chatter: TwinChatter, conversations_folder: str) -> None:
        self.__list_trainer = ListTrainer(twin_chatter.chat_bot)
        self.__conversations = self.import_conversations(conversations_folder)

    @staticmethod
    def import_conversations(conversations_folder: str) -> List[List[Dict[str, object]]]:
        conversations = []

        for file in listdir(conversations_folder):
            conversation_file = path.join(conversations_folder, file)

            with open(conversation_file, 'r', encoding='utf-8') as conversation:
                conversations.append(json.load(conversation))

        return conversations
    
    def train(self) -> None:
        for conversation in self.__conversations:
            for entry in conversation:
                statements = entry.get('statements')
                response = entry.get('response')

                for statement in statements:
                    self.__list_trainer.train([statement, response])
