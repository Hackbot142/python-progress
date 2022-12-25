import requests
import json

api_key = 'YOUR_API_KEY_HERE'
# sign up for api here and also change location https://home.openweathermap.org/users/sign_up
location = 'New York, US'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')
data = response.json()
temperature = data['main']['temp'] - 273.15
description = data['weather'][0]['description']

print(f'The weather in {location} is currently {description} with a temperature of {temperature:.1f}°C.')