import sqlite3
from dotenv import load_dotenv
import os
from pathlib import Path

# Caminho absoluto até o diretório principal onde o .env está localizado
env_path = Path(__file__).resolve().parent.parent / '.env'

# Carregando variáveis de ambiente
load_dotenv(dotenv_path=env_path)

DB_Nome = os.getenv('DB_NAME')

conexao = sqlite3.connect(f"{DB_Nome}.db")
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    usuario TEXT UNIQUE NOT NULL,
                    nome TEXT NOT NULL,
                    senha TEXT NOT NULL
                )
            ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS medidas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT,
                    peso REAL,
                    ombro REAL,
                    peito REAL,
                    braco REAL,
                    antebraco REAL,
                    cintura REAL,
                    quadril REAL,
                    coxa REAL,
                    panturrilha REAL, 
                    usuario INTEGER,
                    FOREIGN KEY (usuario) REFERENCES usuarios(id) ON DELETE CASCADE
                )       
            ''')

cursor.execute("insert into usuarios (usuario, nome, senha) values (?,?,?)",("Fufu","Fulano","123"))
cursor.execute("insert into usuarios (usuario, nome, senha) values (?,?,?)",("Cici","Ciclano","123"))

conexao.commit()
conexao.close()