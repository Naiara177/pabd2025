#!/usr/bin/env bash
# Script simples para validar as variáveis de ambiente do Supabase e testar uma requisição
set -e
if [ -z "$SUPABASE_URL" ] || [ -z "$SUPABASE_KEY" ]; then
  echo "Variáveis SUPABASE_URL e SUPABASE_KEY não definidas. Copie .env.example para .env e preencha." >&2
  exit 2
fi
python - <<'PY'
from empresa.config.database import SupabaseConnection
try:
    client = SupabaseConnection().client
    resp = client.table('departamento').select('*').execute()
    print('Probe response OK:', getattr(resp, 'status_code', 'no-status'), getattr(resp, 'data', None))
except Exception as e:
    print('Erro ao testar Supabase:', e)
    raise
PY
