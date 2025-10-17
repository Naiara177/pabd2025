# Modúlo de conexão com o supabase 
import os 
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega as variaveis de ambiente 
load_dotenv()   

class SupabaseConnection:
    ''' padrão de projeto - Dingleton
      * garante apenas uma instancia 
        em toda a aplicação '''
    __instance = None
    #Type Hint - garante o tipo de dado 
    #a ser atribuido ao um atributo ou variavel
    _client: Client = None
    # nem - cria a instância da classe
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SupabaseConnection, cls).__new__(cls)
            cls.__instance._init_connection()
        return cls.__instance

    def _init_connection(self):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')

        if not supabase_url or not supabase_key:
            raise ValueError("Erro nas variáveis de ambiente.")

        self._client = create_client(supabase_url, supabase_key)
        print("Conexão com Supabase OK!!!.")

    @property
    def client(self) -> Client:  #Type Hint
        return self._client