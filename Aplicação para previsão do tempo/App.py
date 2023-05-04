from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/previsao')
def previsao():
    cidade = request.args.get('cidade')
    estado = request.args.get('estado')

    # Obter as coordenadas da cidade e estado usando a API do OpenCage Geocoder
    geocoder_api_key = '40a1620a72804e6dbf9df93cce8d8d10'
    geocoder_url = f'https://api.opencagedata.com/geocode/v1/json?q={cidade}+{estado}&key={geocoder_api_key}'
    response = requests.get(geocoder_url)
    data = response.json()
    lat = data['results'][0]['geometry']['lat']
    lng = data['results'][0]['geometry']['lng']

    # Obter as informações de previsão do tempo usando a API do OpenWeatherMap
    weather_api_key = 'f46a2fd0705ae8c9825f8e76247bec8e'
    weather_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=minutely,hourly,daily,alerts&units=metric&appid={weather_api_key}'

    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()
        temperatura = data['current']['temp']
        condicoes = data['current']['weather'][0]['description']
        return jsonify({
            'cidade': cidade,
            'estado': estado,
            'temperatura': temperatura,
            'condicoes': condicoes
        })
    except requests.exceptions.HTTPError as error:
        return jsonify({'erro': f'Erro na chamada da API: {error}'})
    except KeyError as error:
        return jsonify({'erro': f'Erro na resposta da API: {error}'})

if __name__ == '__main__':
    app.run()

