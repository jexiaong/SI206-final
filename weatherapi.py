import requests
import sqlite3
import sys
from secret import WA_API_KEY

def create_table(conn, cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS weatherapi (
            hours INT PRIMARY KEY,
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

def weatherapi():
    location_key = '329380'
    location = 42.2808, 83.7430
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WA_API_KEY}&q=London&days=7"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        sys.exit()

    jsonData = response.json()
    # print(jsonData)

    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    #Create table if it doesn't already exist
    create_table(connection, cursor)

    count = 0
    for day in jsonData['forecast']['forecastday']:
        for hourly_data in day['hour']:
            if count < 25:
                hours = hourly_data['time_epoch']
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
                cursor.execute('SELECT hours FROM weatherapi WHERE hours = ?', (hours,))
                existing_data = cursor.fetchone()

                if not existing_data:
                    count += 1
                    # print(cond_id)

                    cursor.execute('''
                        INSERT INTO weatherapi 
                        (hours, temp_c, wind_kph, wind_degree, pressure_mb, precip_mm, humidity, feelslike_c, chance_of_rain, gust_kph) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''',
                        (hours, temp_c, wind_kph, wind_degree, pressure_mb, precip_mm, humidity, feelslike_c, chance_of_rain, gust_kph))
                    connection.commit()

    cursor.execute('''
        SELECT COUNT(*) FROM weatherapi
        ''')
    rows = cursor.fetchone()[0]
    print(rows)

    connection.close()

if __name__ == "__main__":
    weatherapi()
