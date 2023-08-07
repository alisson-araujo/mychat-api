from abc import ABC, abstractmethod
from src.db.entities.message import Message
from typing import List


class GetMessages(ABC):
    @abstractmethod
    def get_messages(self, cvs_id: int) -> List[Message]:
        pass
