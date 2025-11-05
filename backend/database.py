from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê as variáveis de ambiente
user = os.getenv("MSSQL_USER")
password = os.getenv("MSSQL_PASSWORD")
host = os.getenv("MSSQL_SERVER")
port = os.getenv("MSSQL_PORT")
database = os.getenv("MSSQL_DATABASE")
driver = os.getenv("MSSQL_DRIVER")
encrypt = os.getenv("MSSQL_ENCRYPT")
trust = os.getenv("MSSQL_TRUST_SERVER_CERTIFICATE")

# Codifica a senha, caso contenha caracteres especiais
from urllib.parse import quote_plus
password_encoded = quote_plus(password)

# Monta a string de conexão
DATABASE_URL = (
    f"mssql+pyodbc://{user}:{password_encoded}@{host}:{port}/{database}"
    f"?driver={driver}"
    f"&Encrypt={encrypt}"
    f"&TrustServerCertificate={trust}"
)

# Cria o engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos (tabelas)
Base = declarative_base()

# Gerenciador de sessão para usar com Depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()