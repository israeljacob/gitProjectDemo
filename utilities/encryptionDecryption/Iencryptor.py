from abc import ABC, abstractmethod
class IEncryptor(ABC):
    @abstractmethod
    def encrypt(self, text) -> None:
        pass