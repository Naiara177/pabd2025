# pabd2025

Este repositório contém exemplos de DAOs (Data Access Objects) e modelos para uma aplicação
que consome o Supabase. Há exemplos de CRUD para as tabelas `funcionario` e `departamento` em
`main.py`.

## Conexão com Supabase

1. Crie um arquivo `.env` na raiz do projeto copiando o `.env.example`:

```bash
cp .env.example .env
```

2. Preencha as variáveis `SUPABASE_URL` e `SUPABASE_KEY` no arquivo `.env` com os valores do seu projeto Supabase.

3. Instale dependências (se necessário):

```bash
pip install -r requirements.txt
```

4. Execute o exemplo em `main.py`:

```bash
python main.py
```

Se as variáveis de ambiente estiverem corretas, o script tentará usar o cliente Supabase real. Caso
as credenciais estejam ausentes ou inválidas, o script cairá em um `MockClient` para demonstração
local dos métodos CRUD.

## Notas

- O módulo de conexão está em `empresa/config/database.py`.
- Se desejar, forneça a `service_role` key para permitir operações administrativas (cuidado — essa
	chave dá acesso amplo ao banco).
