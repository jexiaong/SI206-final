import requests

# Replace 'YourAPIKey' and 'YourLocationKey' with your actual AccuWeather API key and location key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9wZmEuZm9yZWNhLmNvbVwvYXV0aG9yaXplXC90b2tlbiIsImlhdCI6MTcwMTgzMjY1NCwiZXhwIjo5OTk5OTk5OTk5LCJuYmYiOjE3MDE4MzI2NTQsImp0aSI6ImM4NTAxYmUwNjQyNjg5NTEiLCJzdWIiOiJqZXhpYW9uZyIsImZtdCI6IlhEY09oakM0MCtBTGpsWVR0amJPaUE9PSJ9.MNoeWRihos1dmkFQN93nWb4QfG5xrvz3LCSkUX-qgpc'
api_key2 = 'aUE9PSJ9.MNoeWRihos1dmkFQN93nWb4QfG5xrvz3LCSkUX-qgpc'
location = 102643743 #'42.2808, 83.7430'


# URL for the hourly forecast API
url = f"https://api.foreca.com/api/v1/forecast/hourly/:{location}?apikey={api_key}"

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