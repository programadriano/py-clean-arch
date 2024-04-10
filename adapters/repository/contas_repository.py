from domain.entities.conta import Conta
from domain.interfaces.repositories import IContasRepository

class ContasRepositoryMemoria(IContasRepository):
    def obter_conta_por_id(self, conta_id: int) -> Conta:
        return Conta(conta_id,"Thiago Adriano", 100.0)