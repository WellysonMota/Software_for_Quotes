import requests

def get_dolar_value():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates']['BRL']
    except requests.RequestException as e:
        print(f'An error occurred: {e}')
        return None

if __name__ == '__main__':
    rint(get_dolar_value())