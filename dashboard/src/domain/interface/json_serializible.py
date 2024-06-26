from abc import ABC, abstractmethod

class JsonSerializableInterface(ABC):

    @abstractmethod
    def to_json(self) -> dict: pass

    def identifier(self) -> str: pass
    