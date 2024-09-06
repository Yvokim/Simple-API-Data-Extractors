import requests

api_key = 'f049c6c3754591944cd36504f0b40f08'

city = 'Nairobi'

# API endpoint for current weather data
url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=f049c6c3754591944cd36504f0b40f08'

# Make a GET request to the API

response = requests.get(url)

if response.status_code == 200:
    # parse JSON response
    data = response.json()

    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    # Display weather info
    print(f'Current weather in {city}:')
    print(f'Temperature: {temperature} K')
    print(f'Description:{description}')
    print(f'humidity: {humidity}')

else:
    print('Error fetching weather data.Please check your API key or city')

# Extract relevant weather info
