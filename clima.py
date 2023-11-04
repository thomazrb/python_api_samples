import requests
import matplotlib.pyplot as plt

url = 'https://api.open-meteo.com/v1/forecast?latitude=-18.7436941&longitude=-39.9089802&hourly=temperature_2m&timezone=America%2FSao_Paulo&forecast_days=1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    time = data["hourly"]["time"]
    temperature = data["hourly"]["temperature_2m"]
    print(time)
    print(temperature)

    formatted_time = [t.split('T')[1] for t in time]
    print(formatted_time)

    plt.figure(figsize=(12, 4))
    plt.plot(formatted_time, temperature, marker='o', linestyle='-', color='b')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.title('Temperatura do Dia')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura (°C)')
    plt.tight_layout()
    plt.show()

elif response.status_code == 404:
    print('Não encontrado!')
else:
    print('Outro erro!')
    print('Erro: ', response.status_code)