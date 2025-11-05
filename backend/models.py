from sqlalchemy import Column, Integer, String, DateTime, func
from backend.database import Base  # <-- caminho absoluto baseado na estrutura do seu projeto

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(160), nullable=False)
    mensagem = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.sysutcdatetime())
