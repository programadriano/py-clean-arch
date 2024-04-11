from domain.interfaces.repository import IContasRepository
from isNullOrEmpty.is_null_or_empty import is_null_or_empty


class ConsultarSaldoUseCase:
    def __init__(self, repo: IContasRepository):
        self.repo = repo

    def execute(self, conta_id: int) -> float:
        conta = self.repo.obter_conta_por_id(conta_id)
        if is_null_or_empty(conta):
            raise Exception("Conta não encontrada.")
        return conta.saldo
