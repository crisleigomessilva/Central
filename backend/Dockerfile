# Usar a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir fastapi uvicorn mysql-connector-python sqlalchemy passlib[bcrypt]

# Expõe a porta do Uvicorn
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
