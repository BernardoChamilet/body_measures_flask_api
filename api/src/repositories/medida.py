import sqlite3
from src.config.config import db_nome
import os

db_path = os.path.join(os.path.dirname(__file__), f'../../../db/{db_nome}.db')

# buscarMedidas busca todas as medidas de um usuário
def buscarMedidas(user):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medidas WHERE usuario=?",(user,))
        linhas = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if linhas:
        # Medidas encontradas
        medidas = []
        for linha in linhas:
            medidas.append(dict(linha))
        return medidas, None
    else:
        # Nenhuma medida encontrada
        return None, None

# buscarMedida busca uma medida pelo seu id
def buscarMedida(id):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medidas WHERE id=?",(id,))
        medida = cursor.fetchone()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if medida != None:
        # Medida encontrada
        return dict(medida), None
    else:
        # Nenhuma medida encontrada
        return None, None

# buscarDono busca o dono da medida pelo id da medida    
def buscarDono(id):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT usuario FROM medidas WHERE id=?",(id,))
        dono = cursor.fetchone()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if dono != None:
        # Medida encontrada
        return dono[0], None
    else:
        # Nenhuma medida encontrada
        return None, None

# inserirMedida insere uma nova medida de um usuário
def inserirMedida(medidas, user):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medidas (data, peso, ombro, peito, braco, antebraco, cintura, quadril, coxa, panturrilha, usuario) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(medidas['data'],medidas['peso'],medidas['ombro'],medidas['peito'],medidas['braco'],medidas['antebraco'],medidas['cintura'],medidas['quadril'],medidas['coxa'],medidas['panturrilha'],user))
        ultimo_id = cursor.lastrowid
        conn.commit()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    # Medida criada, retornando id
    return ultimo_id, None

# atualizarMedida atualiza dados de uma medida
def atualizarMedida(medidas, id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE medidas SET data=?, peso=?, ombro=?, peito=?, braco=?, antebraco=?, cintura=?, quadril=?, coxa=?, panturrilha=? where id=?",(medidas['data'],medidas['peso'],medidas['ombro'],medidas['peito'],medidas['braco'],medidas['antebraco'],medidas['cintura'],medidas['quadril'],medidas['coxa'],medidas['panturrilha'], id))
        numLinhasAlteradas = cursor.rowcount
        conn.commit()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if numLinhasAlteradas > 0:
        # Sucesso, medida atualizada
        return None, None
    else:
        # Nenhuma medida com esse id encontrada
        return 0, None
    
# deletarMedida deleta uma medida    
def deletarMedida(id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM medidas WHERE id=?",(id,))
        numLinhasAlteradas = cursor.rowcount
        conn.commit()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if numLinhasAlteradas > 0:
        # Medida deletada
        return None, None
    else:
        # Nenhuma medida com esse id encontrada
        return 0, None 