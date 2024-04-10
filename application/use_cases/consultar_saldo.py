from domain.interfaces.repositories import IContasRepository


class ConsultarSaldoUseCase:
    def __init__(self, contas_repository: IContasRepository):
        self.contas_repository = contas_repository

    def execute(self, conta_id: int) -> float:
        conta = self.contas_repository.obter_conta_por_id(conta_id)
        if conta is None:
            raise Exception("Conta não encontrada.")
        return conta.saldo
