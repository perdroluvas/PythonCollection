import pandas as pd
import requests
import json
# Assuming data is a JSON string
data = '{"main": {"temp": 31.02, "feels_like": 36.48, "temp_min": 31.02, "temp_max": 31.02, "pressure": 1009, "humidity": 66, "sea_level": 1009, "grnd_level": 1007}}'

# Parse JSON string into a dictionary
data_dict = json.loads(data)


API_KEY = '3c9922e466b7a959e6ce00559be55dde'
CITY = 'Belém'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    weather_list = data['weather']
    weather_data = [{
        'id' : item['id'],
        'main' : item['main'],
        'description' : item['description'],
        'icon' : item['icon']
    } for item in weather_list]


    
    parsed_list = data['main']
    parsed_data = [{
        'temp': data_dict['main']['temp'],
        'feels_like': data_dict['main']['feels_like'],
        'temp_min': data_dict['main']['temp_min'],
        'temp_max': data_dict['main']['temp_max'],
        #'pressure': data_dict['main']['pressure'],
        'humidity': data_dict['main']['humidity'],
        #'sea_level': data_dict['main']['sea_level'],
        #'grnd_level': data_dict['main']['grnd_level']
    }for parsed_data in parsed_list]
    
    print(data)

    df = pd.DataFrame(weather_data)
    print(df)
    df2 = pd.DataFrame(parsed_data)
    print(df2[1:2])
else:
    print('Error: ', response.status_code)
