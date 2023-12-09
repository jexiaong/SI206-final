import requests
import sqlite3
import sys

# Replace 'YourAPIKey' and 'YourLocationKey' with your actual AccuWeather API key and location key
location_key = '329380'
api_key = '25829ac81461451da7142237230612'
location = 42.2808, 83.7430
url = "http://api.weatherapi.com/v1/forecast.json?key=25829ac81461451da7142237230612&q=London&days=7"

# URL for the hourly forecast API

#"http://dataservice.accuweather.com/api/v1/forecast/hourly/:{location}?apikey={api_key}"

def create_table(conn, cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS weatherapi (
            time_epoch INT PRIMARY KEY,
            temp_c REAL,
            wind_kph REAL,
            wind_degree REAL,
            pressure_mb REAL,
            precip_mm REAL,
            humidity REAL,
            feelslike_c REAL,
            chance_of_rain REAL,
            gust_kph REAL
        )
    ''')
    conn.commit()

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    jsonData = response.json()
    print(jsonData)
else:
    # If the request was not successful, print the error status code
    print(f"Error: {response.status_code}")
# print(jsonData)

connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

#Create table if it doesn't already exist
create_table(connection, cursor)

count = 0
for day in jsonData['days']:
    for hourly_data in day['hours']:
        if count < 25:
            time_epoch = hourly_data['time_epoch']
            temp_c = hourly_data['temp_c']
            wind_kph = hourly_data['wind_kph']
            wind_degree = hourly_data['wind_degree']
            pressure_mb = hourly_data['pressure_mb']
            precip_mm = hourly_data['precip_mm']
            humidity = hourly_data['humidity']
            feelslike_c = hourly_data['feelslike_c']
            chance_of_rain = hourly_data['chance_of_rain']
            gust_kph = hourly_data['gust_kph']

            # Check if the data already exists in the table
            cursor.execute('SELECT time_epoch FROM weatherapi WHERE time_epoch = ?', (time_epoch,))
            existing_data = cursor.fetchone()

            if not existing_data:
                count += 1
                # print(cond_id)

                cursor.execute('''
                    INSERT INTO weatherapi 
                    (time_epoch, temp_c, wind_kph, wind_degree, pressure_mb, precip_mm, humidity, feelslike_c, chance_of_rain, gust_kph) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (time_epoch, temp_c, wind_kph, wind_degree, pressure_mb, precip_mm, humidity, feelslike_c, chance_of_rain, gust_kph))
                connection.commit()

cursor.execute('''
    SELECT COUNT(*) FROM weatherapi
    ''')
rows = cursor.fetchone()[0]
print(rows)

connection.close()
