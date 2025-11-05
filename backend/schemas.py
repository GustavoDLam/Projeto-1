from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class SubmissionIn(BaseModel):
    nome: str
    email: EmailStr
    mensagem: Optional[str] = None

# Dados que a API retorna após salvar no banco
class SubmissionOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    mensagem: str
    created_at: datetime

    class Config:
        orm_mode = True  # Permite conversão automática do modelo SQLAlchemy para o modelo Pydantic
