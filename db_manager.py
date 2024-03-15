import mysql.connector
from mysql.connector import Error

def criar_conexao():
    """Cria uma conexão com o banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='199329',
            database='mydb'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def inserir_quote(data, customer, usd, brl):
    """Insere um novo registro na tabela QuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "INSERT INTO QuoteSent (Data, Customer, USD, brl) VALUES (%s, %s, %s, %s)"
        valores = (data, customer, usd, brl)
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Quote adicionada com sucesso. ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Erro ao inserir quote: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def consultar_quotes():
    """Consulta todos os registros na tabela QuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "SELECT * FROM QuoteSent"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
    except Error as e:
        print(f"Erro ao consultar quotes: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def deletar_quote(id_quote):
    """Deleta um registro específico da tabela QuoteSent pelo idQuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "DELETE FROM QuoteSent WHERE idQuoteSent = %s"
        cursor.execute(query, (id_quote,))
        conexao.commit()
        print(f"Quote com ID {id_quote} deletada com sucesso.")
    except Error as e:
        print(f"Erro ao deletar quote: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Exemplos de uso
if __name__ == '__main__':
    # Inserir uma nova quote
    inserir_quote('2023-03-15', 'Cliente XYZ', 1000.50, brl=0.0 )

    # Consultar todas as quotes
    #consultar_quotes()

    # Deletar uma quote pelo ID
    #deletar_quote(1)
