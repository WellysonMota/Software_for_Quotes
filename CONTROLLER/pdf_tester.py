import pdf_generator


origin = "Brazil"
language = "PT-BR"
currency = "USD"
date = "24-12-2024"
accountmanager = "Welly"
companyname = "EPS"
contactname = "Marcio"
companytype = "Reseller"
companycountry = "Brazil"
companystate ="São Paulo"
companycity = "Campinas"
paymenterm = "NET30"
freight = "incluso"
totalamount = 20000000


pdf_generator.PDF_Generator(origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate, companycity, paymenterm, freight, totalamount)