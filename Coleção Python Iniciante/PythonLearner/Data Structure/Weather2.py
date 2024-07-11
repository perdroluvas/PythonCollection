import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests


def city_chooser():
    available_cities = {
        0: 'Belém',
        1: 'London',
        2: 'Tokyo',
    }
    escolha = False
    while escolha == False:
        city = int(input('Escolha uma cidade: \n0 - Belém\n1 - London\n2 - Tokyo\n'))
        if city in available_cities:
            escolha = True
            return available_cities[city]
        else:
            print('Tente novamente.')


CITY = city_chooser()
API_KEY = '3c9922e466b7a959e6ce00559be55dde'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Extract and format the forecast data
    forecast_list = data['list']
    forecast_data = [{
        'Date': item['dt_txt'],
        'Temperature': item['main']['temp'],
        'Humidity': item['main']['humidity'],
        'Pressure': item['main']['pressure'],
        'Weather': item['weather'][0]['description']
    } for item in forecast_list]

    # Convert to DataFrame
    df = pd.DataFrame(forecast_data)
    temperatura = np.array(df['Temperature'])

    # Calculate mean temperature
    count = 0
    total_sum = 0
    while count < len(temperatura):
        total_sum += temperatura[count]
        count += 1
    if count > 0:
        mean_temperature = total_sum / count
        mean_temperature_str = "{:.5f}".format(mean_temperature)
        print("Mean Temperature:", mean_temperature_str)

    # Print the result
    mean_temperature = np.mean(temperatura)
    print("Mean Temperature:", mean_temperature)



else:
    print(f"Error: {response.status_code}")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot temperature over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Weather', data=df)
plt.title('Temperature Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.show()
