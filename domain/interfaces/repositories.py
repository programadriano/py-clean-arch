from abc import ABC, abstractmethod

class IContasRepository(ABC):
    @abstractmethod
    def obter_conta_por_id(self, conta_id: int):
        pass