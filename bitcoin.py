import requests
from datetime import datetime

def converter_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%a %d-%m-%Y %I:%M:%S %p')

url = 'https://www.mercadobitcoin.net/api/ticker'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    ticker_data = data.get("ticker")
    if ticker_data:
        print("Preço de compra:", ticker_data["buy"])
        print("Preço de venda:", ticker_data["sell"])
        print("Preço mais alto:", ticker_data["high"])
        print("Preço mais baixo:", ticker_data["low"])
        print("Preço de abertura:", ticker_data["open"])
        print("Último preço:", ticker_data["last"])
        print("Volume de negociação:", ticker_data["vol"])
        print("Data:", converter_timestamp(ticker_data["date"]))
    else:
        print("Dados do ticker não encontrados na resposta da API")

elif response.status_code == 404:
    print('Não encontrado!')
else:
    print('Outro erro!')
    print('Erro: ', response.status_code)