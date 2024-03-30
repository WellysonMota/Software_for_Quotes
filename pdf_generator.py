import datetime
import os
import subprocess

from fpdf import FPDF  # Certifique-se de ter a biblioteca fpdf instalada


def PDF_Generator(origin, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
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

