import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import about
import clientes
import db_manager_teste
import dolarnow
import button_Controller

def setDatabase_view():

    # Crie uma janela principal
    janela_database = tk.Tk()
    janela_database.title("Configurar Banco de Dados")
    largura = 600
    altura = 400
    x = (janela_database.winfo_screenwidth() - largura) // 2
    y = (janela_database.winfo_screenheight() - altura) // 2
    janela_database.geometry(f"{largura}x{altura}+{x}+{y}")

    label_passcode = tk.Label(janela_database, text="Insira o Passcode para Editar o Banco:")
    label_passcode.grid(row=1, column=0, padx=0, pady=0)
    passcode_input = tk.Entry(janela_database)  # Campo para digitar a entrada
    passcode_input.grid(row=2, column=0, padx=0, pady=0)

    label_passcode = tk.Label(janela_database, text="Insira os dados do banco de Dados:")
    label_passcode.grid(row=4, column=0, padx=0, pady=0)

    label_host = tk.Label(janela_database, text="Insira o Host:")
    label_host.grid(row=6, column=0, padx=0, pady=0)
    host_input = tk.Entry(janela_database)  # Campo para digitar a entrada
    host_input.grid(row=7, column=0, padx=0, pady=0)

    label_user = tk.Label(janela_database, text="Insira o User:")
    label_user.grid(row=8, column=0, padx=0, pady=0)
    user_input = tk.Entry(janela_database)  # Campo para digitar a entrada
    user_input.grid(row=9, column=0, padx=0, pady=0)

    label_password = tk.Label(janela_database, text="Insira o Password do Banco:")
    label_password.grid(row=10, column=0, padx=0, pady=0)
    password_input = tk.Entry(janela_database)  # Campo para digitar a entrada
    password_input.grid(row=11, column=0, padx=0, pady=0)

    label_database = tk.Label(janela_database, text="Insira o Database")
    label_database.grid(row=12, column=0, padx=0, pady=0)
    database_input = tk.Entry(janela_database)  # Campo para digitar a entrada
    database_input.grid(row=13, column=0, padx=0, pady=0)

    button = tk.Button(janela_database, width=14, height=1, text="Configurar Banco  ", command=lambda: db_manager_teste.databaseChange(passcode_input.get(), host_input.get(), user_input.get(), password_input.get(), database_input.get()) )
    button.grid(row=17, column=0, padx=8, pady=5, sticky="w")





    janela_database.mainloop()
