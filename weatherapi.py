import requests

# Replace 'YourAPIKey' and 'YourLocationKey' with your actual AccuWeather API key and location key
location_key = '329380'
api_key = '25829ac81461451da7142237230612'
location = 42.2808, 83.7430
url = "http://api.weatherapi.com/v1/current.json?key=25829ac81461451da7142237230612&q=London"

# URL for the hourly forecast API

#"http://dataservice.accuweather.com/api/v1/forecast/hourly/:{location}?apikey={api_key}"

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