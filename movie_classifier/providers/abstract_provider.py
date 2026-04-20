from abc import ABC, abstractmethod


class Provider(ABC):
    @abstractmethod
    def invoke(self, summary: str, system_prompt: str) -> str:
        raise NotImplementedError
