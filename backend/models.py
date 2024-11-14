# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id_usuario = Column(Integer, primary_key=True, index=True)  # Chave primária, garantindo unicidade
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=True)
    senha = Column(String(255), nullable=False)  # Senha será armazenada como hash
    pessoa = Column(String(255), nullable=True)  # Campo para informações adicionais futuramente
