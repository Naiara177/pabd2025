from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class Departamento:
    numero: Optional[int]
    nome: str
    localizacao: Optional[str] = None
    gerente_cpf: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        # Converter datetimes para ISO strings para envio ao supabase, se necessário
        if data.get('created_at') and isinstance(data['created_at'], datetime):
            data['created_at'] = data['created_at'].isoformat()
        if data.get('updated_at') and isinstance(data['updated_at'], datetime):
            data['updated_at'] = data['updated_at'].isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Departamento':
        if data is None:
            return None
        created = data.get('created_at')
        updated = data.get('updated_at')
        # Tentar parsear strings ISO para datetime quando aplicável
        try:
            if isinstance(created, str):
                created = datetime.fromisoformat(created)
        except Exception:
            created = created
        try:
            if isinstance(updated, str):
                updated = datetime.fromisoformat(updated)
        except Exception:
            updated = updated

        return cls(
            numero=data.get('numero') or data.get('id') or None,
            nome=data.get('nome') or data.get('descricao') or '',
            localizacao=data.get('localizacao'),
            gerente_cpf=data.get('gerente_cpf') or data.get('cpf_gerente') or None,
            created_at=created,
            updated_at=updated,
        )

    def __str__(self) -> str:
        return f"Departamento(numero={self.numero}, nome={self.nome})"
