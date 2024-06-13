import datetime
import os
import subprocess

from fpdf import FPDF  # Certifique-se de ter a biblioteca fpdf instalada

import pandas as pd
from tabulate import tabulate


produtos = [
    {"Nome": "IPad", "Preço": 1200, "Quantidade": 1000},
    {"Nome": "Iphone", "Preço": 3000, "Quantidade": 60},
    {"Nome": "AppleWatch", "Preço": 2600, "Quantidade": 5000},
]

table = pd.DataFrame(produtos)
table.style \
    .format(precision=3, thousands=".", decimal=",")\
    .format_index(str.upper, axis=1) \
    .relabel_index(["row 1", "row 2", "row 3"], axis =0)
tabela = tabulate(produtos, headers="keys", tablefmt="fancy_grid")


folder_path = 'generated_quotes'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def PDF_Generator(origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                  companycity, paymenterm, freight, totalamount):

#Classificação do Header de acordo com a origim selecionada.
    if origin == "Brasil":
        headerQuote : str  = "EPS Serviços para Produtos Eletrônicos do Brasil LTDA - CNPJ: 14.150.26/0001-70 - Tel.: +55 19 3256-0661"
    elif origin == "Estados Unidos":
        headerQuote: str = "EPS Services LLC - TAX ID xxxxxxx - Phone: xxxxxxxxxxxxxxxxxx - Indianapolis US"
    elif origin == "Irlanda":
        headerQuote: str = "EPS Services LLC - TAX ID xxxxxxx - Phone: xxxxxxxxxxxxxxxxxx - Dublin - IE"
    else:
        headerQuote: str  = "Error please select another location"

    # Classificação da linguagem da proposta
    if language == "PT-BR":
            helloQuote: str = f"Prezado(a) {contactname}, obrigado por sua solicitação, por gentileza avalie nossa proposta abaixo:"
    elif language == "EN-US":
            helloQuote: str = f"Hi {contactname}, thank you for your request, please see our proposal below:"
    elif language  == "ES-AR":
            helloQuote: str = "Estimado, gracias por su solicitud, por favor evalúe nuestra propuesta a continuación:"
    else:
            helloQuote: str = "Error please select another language"

    class PDF(FPDF):

        def header(self):
            self.set_font("Arial", "B", 8)
            self.cell(0, 4, f"{headerQuote}", 0, 1, "L")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Cliente: {contactname}", 0, 0, "L")
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    datahoje = datetime.date.today()
    data_formatada = datahoje.strftime("%d-%m-%Y")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, f"Data: {data_formatada}", align="R")
    pdf.multi_cell(0, 10, f"Cliente: {contactname}")
    pdf.multi_cell(0, 10, f"Empresa: {companyname}")
    pdf.multi_cell(0, 10, f"Local: {companycountry}")
    pdf.multi_cell(0, 10, f"Moeda: {currency}")
    pdf.multi_cell(0, 10, f"Termo de Pagamento: {paymenterm}")
    pdf.multi_cell(0, 10, f"Frete: {freight}")
    pdf.multi_cell(0, 10, f"{helloQuote}")
    pdf.multi_cell(0, 10, f"{table}",  align="C")


    nome_arquivo = f"Cotacao {companyname} {origin} - {data_formatada}.pdf"

    try:
        pdf.output(nome_arquivo)
        print("PDF gerado com sucesso!")

        if os.path.exists(nome_arquivo):
            # Abra o arquivo PDF no leitor de PDF padrão
            ## subprocess.Popen([nome_arquivo], shell=True) == PARA WINDOWS
            subprocess.Popen(["xdg-open", nome_arquivo]) #PAra Linux!!!!
        else:
            print("PDF Não foi aberto, arquivo não existe")
            mensagem = "PDF Não foi aberto, arquivo não existe"
    except:
        print("PDF Não foi gerado, arquivo Aberto")

