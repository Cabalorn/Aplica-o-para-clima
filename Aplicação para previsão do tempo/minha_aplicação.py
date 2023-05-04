import pandas as pd
import requests

# Chaves de API do OpenCage Geocoder e OpenWeatherMap
OPENCAGE_API_KEY = '40a1620a72804e6dbf9df93cce8d8d10'
OPENWEATHER_API_KEY = 'f46a2fd0705ae8c9825f8e76247bec8e'

# Função para obter as coordenadas geográficas da cidade fornecida pelo usuário
def obter_coordenadas(cidade):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={cidade}&key={OPENCAGE_API_KEY}'

    response = requests.get(url).json()

    lat = response['results'][0]['geometry']['lat']
    lng = response['results'][0]['geometry']['lng']

    return lat, lng

# Função para obter a previsão do tempo para as coordenadas fornecidas
def obter_previsao_tempo(lat, lng):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&units=metric&appid={OPENWEATHER_API_KEY}'

    response = requests.get(url).json()

    temperatura = response['main']['temp']
    condicao = response['weather'][0]['description']
    umidade = response['main']['humidity']
    velocidade_vento = response['wind']['speed']

    return temperatura, condicao, umidade, velocidade_vento
