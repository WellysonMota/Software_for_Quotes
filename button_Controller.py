import pdf_generator
import db_manager


def gerarQuote_Action (origin, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                       companycity, paymenterm, freight, totalamount):

    #Função 1 = Armazenar Valores no Banco

    db_manager.inserir_quote(origin, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                            companycity, paymenterm, freight, totalamount)

    # Função 2 = Gerar PDF

    #pdf_generator.PDF_Generator(origin, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                              #  companycity, paymenterm, freight, totalamount)