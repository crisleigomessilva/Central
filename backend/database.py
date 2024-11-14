# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User
from passlib.context import CryptContext

DATABASE_URL = "mysql+mysqlconnector://root:12007167@db/centralsousys"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação do contexto para hashing de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para criar o hash da senha
def get_password_hash(password):
    return pwd_context.hash(password)

# Função para inicializar o banco de dados
def init_db():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Adiciona o usuário padrão
    db = SessionLocal()
    try:
        # Verifica se o usuário admin já existe
        admin_user = db.query(User).filter_by(email="crislei@sousys.com.br").first()
        if not admin_user:
            # Se o usuário não existir, cria-o
            admin_user = User(
                nome="admin",
                email="crislei@sousys.com.br",
                senha=get_password_hash("123456"),  # Hash da senha
                telefone="",
                pessoa="admin"
            )
            db.add(admin_user)
            db.commit()
    finally:
        db.close()

# Dependência de sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
