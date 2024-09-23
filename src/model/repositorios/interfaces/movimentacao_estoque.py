import abc
from datetime import datetime
from src.model.model.estoque import MovimentoDeEstoque


class MovimentacaoDeEstoque(abc.ABC):
    @abc.abstractmethod
    def buscar_movimentacao(self, dt_inicial: datetime, dt_final: datetime) -> MovimentoDeEstoque:
        pass