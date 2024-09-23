from datetime import datetime
from src.model.repositorios.interfaces.movimentacao_estoque import MovimentacaoDeEstoque


class BuscarMovimentacaoController:
    def buscar_movimento(self, dt_inicial: datetime, dt_final: datetime, repository: MovimentacaoDeEstoque) -> None:
        movimento = repository.buscar_movimentacao(dt_inicial=dt_inicial, dt_final=dt_final)
        