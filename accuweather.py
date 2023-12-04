

import requests

# Replace 'YourAPIKey' and 'YourLocationKey' with your actual AccuWeather API key and location key
api_key = '329380'
location_key = 'ExjKml3Q1PDHprqCGOVs5OnyWwFcxrRH'

# URL for the hourly forecast API
url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/120hour/{location_key}?apikey={api_key}'

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    
    # Now, 'json_data' contains the hourly forecast data in JSON format
    print(json_data)
else:
    # If the request was not successful, print the error status code
    print(f"Error: {response.status_code}")