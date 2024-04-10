from fastapi import FastAPI, HTTPException
from application.use_cases.consultar_saldo import ConsultarSaldoUseCase
from adapters.repository.contas_repository import ContasRepositoryMemoria
from infrastructure.logging.logging_config import setup_logging
import logging

# Configuração do Logging
setup_logging()
logger = logging.getLogger(__name__)

# Inicialização do FastAPI
app = FastAPI(title="Finanças Clean Architecture", version="1.0.0")

# Inicialização do repositório
contas_repo = ContasRepositoryMemoria()

@app.on_event("startup")
async def startup_event():
    logger.info("Iniciando aplicação...")

@app.get("/contas/{conta_id}/saldo", summary="Consulta o saldo de uma conta")
def consultar_saldo(conta_id: int):
    logger.info(f"Recebida solicitação de saldo para a conta {conta_id}")
    use_case = ConsultarSaldoUseCase(contas_repo)
    try:
        saldo = use_case.execute(conta_id)
        logger.info(f"Saldo consultado para conta {conta_id}: {saldo}")
        return {"conta_id": conta_id, "saldo": saldo}
    except Exception as e:
        logger.error(f"Erro ao consultar saldo para conta {conta_id}: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Finalizando aplicação...")