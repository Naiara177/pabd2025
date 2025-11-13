from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from datetime import datetime, date


@dataclass
class Funcionario:
    cpf: str
    pnome: str
    unome: str
    data_nasc: Optional[date] = None
    endereco: Optional[str] = None
    salario: Optional[float] = None
    sexo: Optional[str] = None
    cpf_supervisor: Optional[str] = None
    numero_departamento: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        if data.get('created_at') and isinstance(data['created_at'], datetime):
            data['created_at'] = data['created_at'].isoformat()
        if data.get('updated_at') and isinstance(data['updated_at'], datetime):
            data['updated_at'] = data['updated_at'].isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Funcionario':
        if data is None:
            return None
        created = data.get('created_at')
        updated = data.get('updated_at')
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
            cpf=data.get('cpf') or data.get('id'),
            pnome=data.get('pnome') or data.get('primeiro_nome') or '',
            unome=data.get('unome') or data.get('ultimo_nome') or '',
            data_nasc=data.get('data_nasc'),
            endereco=data.get('endereco'),
            salario=data.get('salario'),
            sexo=data.get('sexo'),
            cpf_supervisor=data.get('cpf_supervisor'),
            numero_departamento=data.get('numero_departamento'),
            created_at=created,
            updated_at=updated,
        )

    def __str__(self) -> str:
        return f"Funcionario(cpf={self.cpf}, nome={self.pnome} {self.unome})"
