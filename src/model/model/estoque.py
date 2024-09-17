import pandas as pd


class MovimentoDeEstoque:
    __columns_names: set = {
        'nro_documento',
        'tipo_movimento',
        'cod_parceiro',
        'segmento',
        'cidade',
        'data_movimento',
        'cod_produto',
        'descricao',
        'marca',
        'secao',
        'grupo',
        'qtd_negociada',
        'vlr_unitario',
        'vlr_desconto'
    }

    def __init__(self, movimento: pd.DataFrame) -> None:
        self.__movimento = self.__validate_dataframe(movimento)
        self.__clear_dataframe()
    
    def __validate_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        if not self.__columns_names.issubset(dataframe.columns):
            raise Exception('A estrutura de dados não corresponde ao formato exigido.')
        return dataframe
    
    def __clear_dataframe(self):
        self.__movimento['descricao'] = self.__movimento['descricao'].str.capitalize()
        self.__movimento['marca'] = self.__movimento['marca'].str.capitalize()
        self.__movimento['data_movimento'] = pd.to_datetime(self.__movimento['data_movimento'], format='%d/%m/%Y %H:%M:%S')
