import mysql.connector
from tkinter import ttk

def fetch_ultimas_cotacoes():
    """
    Busca as últimas 10 cotações do banco de dados.
    """
    try:
        connection = mysql.connector.connect(
            host='seu_host',
            user='seu_usuario',
            password='sua_senha',
            database='seu_banco'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT id, data, cliente, empresa, valor_total FROM cotacoes ORDER BY data DESC LIMIT 10")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Erro ao conectar no banco de dados: {e}")
        return []
    finally:
        if connection:
            connection.close()

def atualizar_tabela():
    """
    Atualiza o Treeview com os dados mais recentes.
    """
    for row in tree.get_children():
        tree.delete(row)
    dados = fetch_ultimas_cotacoes()
    for linha in dados:
        tree.insert("", "end", values=linha)

# Configuração do Treeview
tree = ttk.Treeview(right_pane, columns=("ID", "Data", "Cliente", "Empresa", "Valor Total"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Data", text="Data")
tree.heading("Cliente", text="Cliente")
tree.heading("Empresa", text="Empresa")
tree.heading("Valor Total", text="Valor Total")

tree.column("ID", width=50, anchor="center")
tree.column("Data", width=100, anchor="center")
tree.column("Cliente", width=150, anchor="w")
tree.column("Empresa", width=150, anchor="w")
tree.column("Valor Total", width=100, anchor="center")

# Scrollbar para a tabela
scrollbar = ttk.Scrollbar(right_pane, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Posicionamento no painel direito
tree.grid(row=21, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
scrollbar.grid(row=21, column=3, sticky="ns", padx=0, pady=10)

# Atualizar a tabela ao iniciar
atualizar_tabela()
