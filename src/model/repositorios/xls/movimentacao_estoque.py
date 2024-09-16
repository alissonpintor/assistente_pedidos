import os
import pathlib
import pandas as pd
from datetime import datetime
from src.model.model.estoque import MovimentoDeEstoque
from src.model.repositorios.interfaces.movimentacao_estoque import MovimentacaoDeEstoque


class MovimentacaoDeEstoqueXls(MovimentacaoDeEstoque):
    __columns_names: set = {
        'nro_documento',
        'tipo_movimento',
        'cod_parceiro',
        'data_movimento',
        'cod_produto',
        'descricao',
        'marca',
        'qtd_negociada',
        'vlr_unitario',
        'vlr_desconto'
    }

    def buscar_movimentacao(self, dt_inicial: datetime, dt_final: datetime) -> MovimentoDeEstoque:
        xls_filepath = os.environ.get('XLS_FILE_PATH', None)
        xls_filepath = self.__validate_file(xls_filepath)

        dataframe = pd.read_csv(xls_filepath)

        movimento: MovimentoDeEstoque = MovimentoDeEstoque(dataframe)
        return movimento

    
    def __validate_file(self, xls_filepath: str | None) -> pathlib.Path:
        cwd = pathlib.Path.cwd()

        if not xls_filepath:
            raise Exception('O xls com os dados não foi informado.')
        
        file = cwd / xls_filepath
        
        if not os.path.exists(file):
            raise Exception('O xls informado não foi encontrado')
        
        return file