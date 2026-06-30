from abc import ABC, abstractmethod


class BaseTTSModel(ABC):

    @abstractmethod
    def speak(self, text: str, output_path: str):
        pass