import sqlite3
from src.config.config import db_nome
import os

db_path = os.path.join(os.path.dirname(__file__), f'../../../db/{db_nome}.db')

# buscarUsuario busca dados não sensíveis de um usuário
def buscarUsuario(id):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT usuario, nome FROM usuarios WHERE id=?",(id,))
        usuario = cursor.fetchone()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if usuario == None:
        # Usuário não encontrado
        return None, None
    # Usuário encontrado
    return dict(usuario), None
    
# buscarUsuarios busca dados de todos usuários, exceto senhas
def buscarUsuarios():
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT usuario, nome FROM usuarios")
        linhas = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if linhas:
        # Usuarios encontrados
        usuarios = []
        for linha in linhas:
            usuarios.append(dict(linha))
        return usuarios, None
    else:
        # Nenhum usuário encontrado
        return None, None

# criarUsuario insere um novo usuário no banco de dados    
def criarUsuario(usuario):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, nome, senha) VALUES (?,?,?)",(usuario['usuario'], usuario['nome'], usuario['senha']))
        ultimo_id = cursor.lastrowid
        conn.commit()
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constraint failed: usuarios.usuario' in str(e):
            # Erro de nome de usuário já existente (erro 400 e não 500)
            return None, 409
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    # Usuário criado, retornando id
    return ultimo_id, None

# atualizar usuário atualiza dados de um usuário, exceto a senha
def atualizarUsuario(usuario, id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET usuario=?, nome=? where id=?",(usuario['usuario'], usuario['nome'], id))
        numLinhasAlteradas = cursor.rowcount
        conn.commit()
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constraint failed: usuarios.usuario' in str(e):
            # Erro de nome de usuário já existente (erro 400 e não 500)
            return None, 409
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if numLinhasAlteradas > 0:
        # Sucesso
        return None, None
    else:
        # Nenhuma linha alterada
        return 0, None
    
# atualizarSenha atualiza senha de um usuário    
def atualizarSenha(senha, id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET senha=? where id=?",(senha, id))
        numLinhasAlteradas = cursor.rowcount
        conn.commit()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if numLinhasAlteradas > 0:
        # Sucesso
        return None, None
    else:
        # Nenhuma linha alterada
        return 0, None

# buscarSenha busca a senha de um usuário
def buscarSenha(id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE id=?",(id,))
        senha = cursor.fetchone()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if senha == None:
        # Nenhum usuário com esse id encontrado
        return None, None
    # Sucesso, retornando senha
    return senha[0], None
    
# buscarSenha busca a senha de um usuário usando usuario
def buscarSenhaEIDPeloUser(user):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, senha FROM usuarios WHERE usuario=?",(user,))
        senhaEID = cursor.fetchone()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if senhaEID == None:
        # Nenhum usuário encontrado
        return None, None, None
    # Sucesso, retornando senha
    return senhaEID[1], senhaEID[0], None

# deletarUsuario deleta um usuário
def deletarUsuario(id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=?",(id,))
        numLinhasAlteradas = cursor.rowcount
        conn.commit()
    except sqlite3.DatabaseError as e:
        # Erro interno de servidor
        return None, f"Erro de banco de dados: {e}"
    finally:
        if conn:
            conn.close()
    if numLinhasAlteradas > 0:
        # Linha apagada
        return None, None
    else:
        # Nenhum linha apagada
        return 0, None 