import requests

teste = 1


def buscar_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro ao buscar o CNPJ. Código de status: {response.status_code}")
        return None


cnpj = '14150267000170'

resultado = buscar_cnpj(cnpj)
if resultado:
    print(resultado)
