import requests

url = 'https://www.google.com/'

response = requests.get(url)

if response.status_code == 200:
    print('OK')
    print(response.content)

elif response.status_code == 404:
    print('Não encontrado!')
else:
    print('Outro erro!')