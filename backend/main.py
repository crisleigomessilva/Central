# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import init_db, get_db, User  # Certifique-se de importar o modelo User e a função get_db
from passlib.context import CryptContext

init_db()  # Inicializa o banco de dados
app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Modelo para os dados de login
class LoginData(BaseModel):
    email: str
    password: str

# Função para verificar a senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Rota para autenticação
@app.post("/login")
def login(login_data: LoginData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    return {"message": "Login realizado com sucesso", "user": user.name}

# Rota raiz
@app.get("/")
async def root():
    return {"message": "Backend FastAPI funcionando corretamente!"}

# Rota para testar a conexão com o MySQL
@app.get("/test_db_connection")
async def test_db_connection():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="12007167",
            database="centralsousys",
        )
        if connection.is_connected():
            return {"status": "Connection successful"}
    except Error as e:
        return {"status": "Connection failed", "error": str(e)}
    finally:
        if connection.is_connected():
            connection.close()
