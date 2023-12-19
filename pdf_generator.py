import datetime
import os
import subprocess

from fpdf import FPDF  # Certifique-se de ter a biblioteca fpdf instalada


def PDF_Generator(cliente, empresa, combobox_local, combobox_moeda, combobox_inco, combobox_termo, combobox_frete):
    class PDF(FPDF):

        def header(self):
            self.set_font("Arial", "B", 8)
            self.cell(0, 4, f"Teste Header", 0, 1, "L")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Cliente: {cliente}", 0, 0, "L")
            self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    datahoje = datetime.date.today()
    data_formatada = datahoje.strftime("%d-%m-%Y")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, f"Data: {data_formatada}", align="R")
    pdf.multi_cell(0, 10, f"Cliente: {cliente}")
    pdf.multi_cell(0, 10, f"Empresa: {empresa}")
    pdf.multi_cell(0, 10, f"Local: {combobox_local}")
    pdf.multi_cell(0, 10, f"Moeda: {combobox_moeda}")
    pdf.multi_cell(0, 10, f"Incoterm: {combobox_inco}")
    pdf.multi_cell(0, 10, f"Termo de Pagamento: {combobox_termo}")
    pdf.multi_cell(0, 10, f"Frete: {combobox_frete}")
    nome_arquivo = f"Cotacao {combobox_inco} {empresa} - {data_formatada}.pdf"

    try:
        pdf.output(nome_arquivo)
        print("PDF gerado com sucesso!")

        if os.path.exists(nome_arquivo):
            # Abra o arquivo PDF no leitor de PDF padrão
            subprocess.Popen([nome_arquivo], shell=True)
        else:
            print("PDF Não foi aberto, arquivo não existe")
            mensagem = "PDF Não foi aberto, arquivo não existe"
    except:
        print("PDF Não foi gerado, arquivo Aberto")
