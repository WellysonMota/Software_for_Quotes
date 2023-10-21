import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import clientes
import pdf_generator
import dolarnow

def call_alert(mensagem):
    messagebox.showinfo("Alerta", f"{mensagem}")

def on_button_click():
        dolar_value = dolarnow.get_dolar_value()
        if dolar_value:
            print(f'O valor atual do Dólar é: {dolar_value}')
            label = tk.Label(statusbar, text="")
            label.config(text="")
            label.grid(row=0, column=2, padx=0, pady=0, sticky="w")
            label = tk.Label(statusbar, text=f'O valor atual do Dólar é:      R$ {dolar_value}                       ')
            label.grid(row=0, column=2, padx=0, pady=0,sticky="w")
        else:
            print('Não foi possível obter o valor atual do Dólar.')
            label = tk.Label(statusbar, text="Não foi possível obter o valor do dolar")
            label.grid(row=0, column=2, padx=0, pady=0, sticky="w")


# Crie uma janela principal
janela = tk.Tk()
janela.title("Gerador de Cotações - EPS")
largura = 800
altura = 600
x = (janela.winfo_screenwidth() - largura) // 2
y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Frama para organizar os elementos:

toolbar = tk.Frame(janela, background="#d5e8d4", height=40)
statusbar = tk.Frame(janela, background="#e3e3e3", height=20)
main = tk.PanedWindow(janela, background="#fff")

toolbar.pack(side="top", fill="x")
statusbar.pack(side="bottom", fill="x")
main.pack(side="top", fill="both", expand=True)

left_pane = tk.Frame(main, background="#b2bbc2", width=100)
right_pane = tk.Frame(main, background="#f0f5f5", width=200)
main.add(left_pane)
main.add(right_pane)

#====Configurações da Barra de Superior=================================================================================================
# Use o gerenciador de geometria grid para alinhar os botões à esquerda do toolbar
button = tk.Button(toolbar, text="Carregar Cotação", command="")
button.grid(row=0, column=0, padx=0, pady=0,sticky="w")

button = tk.Button(toolbar, text="Configurações", command="")
button.grid(row=0, column=1, padx=0, pady=0, sticky="w")

button_2 = tk.Button(toolbar, text="About", command="",)
button_2.grid(row=0, column=2, padx=0, pady=0, sticky="w")

#====Configurações da Barra Infrerior (Status Bar) =======================================================================================
button = tk.Button(statusbar, text="Dolar Now", command=lambda: on_button_click())
button.grid(row=0, column=0, padx=0, pady=0, sticky="w")


#====Configurações do Painel direito=======================================================================================
label = tk.Label(right_pane, text="SELECIONE OS DADOS DA EPS")
label.grid(row=0, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Selecione a EPS de Origem:")
label.grid(row=1, column=0, padx=0, pady=0)
localidades = ["Brasil", "Estados Unidos", "Irlanda"]
combobox_local = ttk.Combobox(right_pane, values=localidades)
combobox_local.grid(row=2, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Selecione o Incoterm:   ")
label.grid(row=3, column=0, padx=0, pady=0)
incoterm = ["CIF", "EXW", "FOB", "DDP", "DAP"]
combobox_inco = ttk.Combobox(right_pane, values=incoterm)
combobox_inco.grid(row=4, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Selecione a Moeda:")
label.grid(row=5, column=0, padx=0, pady=0)
lista_moeda = ["BRL", "USD", "EUR",]
combobox_moeda = ttk.Combobox(right_pane, values=lista_moeda)
combobox_moeda.grid(row=6, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Selecione o Account Manager")
label.grid(row=7, column=0, padx=0, pady=0)
lista_manager = ["Welly", "Niall", "Gabi",]
combobox_manager = ttk.Combobox(right_pane, values=lista_manager)
combobox_manager.grid(row=8, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="")
label.grid(row=9, column=0, padx=0, pady=0)
label = tk.Label(right_pane, text="SELECIONE OS DADOS DO CLIENTE")
label.grid(row=10, column=0, padx=0, pady=0)

button = tk.Button(right_pane, text="Buscar Cliente", command="")
button.grid(row=11, column=0, padx=50, pady=10, sticky="w")

label_nomecliente = tk.Label(right_pane, text="Digite o nome do cliente:")
label_nomecliente.grid(row=12, column=0, padx=0, pady=0)
cliente = tk.Entry(right_pane) #Campo para digitar a entrada
cliente.grid(row=13, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Digite o nome da Empresa")
label.grid(row=14, column=0, padx=0, pady=0)
empresa = tk.Entry(right_pane)   #Campo para digitar a entrada
empresa.grid(row=15, column=0, padx=0, pady=0)

label = tk.Label(right_pane, text="Finalidade")
label.grid(row=17, column=0, padx=0, pady=0)
lista_termo = ["Usuario final", "Revenda", "Industrialização",]
combobox_termo = ttk.Combobox(right_pane, values=lista_termo)
combobox_termo.grid(row=18, column=0, padx=0, pady=0)



label = tk.Label(right_pane, text="SELECIONE OS TERMOS DE PAGAMENTO:")
label.grid(row=0, column=1, padx=0, pady=0)


label = tk.Label(right_pane, text="Termo de Pagamento")
label.grid(row=1, column=1, padx=0, pady=0)
lista_termo = ["Antecipado","NET10",  "NET15", "NET20", "NET30", "NET45", "50% Ant + 50% NET30", "50% NET15 + 50% NET30", "50% NET30 + 50% NET45", "50% NET30 + 50% NET60"]
combobox_termo = ttk.Combobox(right_pane, values=lista_termo)
combobox_termo.grid(row=2, column=1, padx=0, pady=0)

label = tk.Label(right_pane, text="Frete")
label.grid(row=3, column=1, padx=0, pady=0)
lista_frete = ["Incluso","Não Incluso", "Sedex", "Transportadora","Motoboy", "Fedex Economy", "Fedex Ground", "Fedex Priority", "Fedex Overnight", ]
combobox_frete = ttk.Combobox(right_pane, values=lista_frete)
combobox_frete.grid(row=4, column=1, padx=0, pady=0)

#====Configurações do PAINEL ESQUERDO (LEFT PANE) =======================================================================================

label = tk.Label(left_pane, text="Cadastrar/Editar")
label.grid(row=0, column=0, padx=0, pady=5)
button = tk.Button(left_pane, text="Clientes  ", width=10, height=1, command=lambda: clientes.ClientesJanela())
button.grid(row=2, column=0, padx=0, pady=5, sticky="w")

button = tk.Button(left_pane, width=10, height=1,text="Produtos  ", command="")
button.grid(row=3, column=0, padx=0, pady=5, sticky="w")

button = tk.Button(left_pane, width=10, height=1,text="Vendedores", command="")
button.grid(row=4, column=0, padx=0, pady=5, sticky="w")





# Botão de Ação final ======================================================================================================================
button = tk.Button(right_pane, text="Gerar PDF", command=lambda: pdf_generator.PDF_Generator(cliente.get(),empresa.get(), combobox_local.get(), combobox_moeda.get(), combobox_inco.get(), combobox_termo.get(), combobox_frete.get()))
button.grid(row=20, column=4, padx=0, pady=0)




janela.mainloop()
