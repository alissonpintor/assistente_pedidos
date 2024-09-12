from email.mime import base
from urllib import response
import requests
import os
from dotenv import load_dotenv

from .exceptions.token_invalido import TokenInvalidoException
from .exceptions.app_key_invalido import AppKeyException
from .exceptions.password_invalido import PasswordException


load_dotenv()


class __Client:
    __instance = None
    __session: requests.Session = requests.session()

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
            cls.__instance.__login()
        return cls.__instance
    
    def __login(self):
        base_url: str | None = 'https://api.sankhya.com.br'
        app_key: str | None = os.environ.get('APP_KEY_SANKHYA')
        token: str | None= os.environ.get('TOKEN_SANKHYA')
        username: str | None = os.environ.get('USER_SANKHYA')
        password: str | None = os.environ.get('PASSWORD_SANKHYA')

        print(app_key)

        if not base_url:
            raise Exception('Você deve informa a url de acesso para a API do Sankhya')

        if not username or not password:
            raise Exception('Você deve informa um usuário e uma senha de acesso para a API do Sankhya')
        
        self.__do_login(base_url, app_key, token, username, password)
    
    def __do_login(self, base_url, app_key, token, username, password):
        '''
        Erros:
            GTW3003: Erro na comunicacao com console.
            4405: appkey inválido
            4303: token inválido
        '''
        headers = {
            'token': token,
            'appkey': app_key,
            'username': username,
            'password': password
        }
        try:
            response = self.__session.post(
                f'{base_url}/login',
                headers=headers
            )
            response = response.json()
            
            if response['error']:
                codigo_erro: str = response['error']['codigo']
                descricao: str = response['error']['descricao']

                if codigo_erro == '4303':
                    raise TokenInvalidoException(f'Erro ao tentar realizar o login no Sankhya. {descricao}')

                if codigo_erro == '4405':
                    raise AppKeyException(f'Erro ao tentar realizar o login no Sankhya. {descricao}')
                
                if codigo_erro == '4':
                    raise PasswordException(f'Erro ao tentar realizar o login no Sankhya. {descricao}')
                
                raise Exception(f'Erro ao tentar realizar o login no Sankhya. {descricao}')
        
        except Exception as e:
            raise e
    
    def is_logged(self) -> bool:
        return True if 'JSESSIONID' in self.__session.cookies else False

    def get(self):
        pass

    def post(self, data):
        pass


client: __Client = __Client.instance()