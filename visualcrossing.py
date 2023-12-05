import requests
import sqlite3
import sys

def create_table(conn, cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visualcrossing (
            datetimeEpoch INT PRIMARY KEY,
            temp REAL,
            feelslike REAL,
            humidity REAL,
            precip REAL,
            precipprob REAL,
            snow REAL,
            snowdepth REAL,
            windgust REAL,
            windspeed REAL,
            winddir REAL,
            pressure REAL,
            visibility REAL,
            cloudcover REAL,
            conditions TEXT
        )
    ''')
    conn.commit()

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Ann%20Arbor%2C%20Michigan?unitGroup=metric&include=hours&key=DXM3T4BUXTSL3WQ47M2PKACHD&contentType=json")

if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()

jsonData = response.json()

connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

#Create table if it doesn't already exist
create_table(connection, cursor)

count = 0
for day in jsonData['days']:
    for hourly_data in day['hours']:
        if count < 25:
            datetimeEpoch = hourly_data['datetimeEpoch']
            # print(datetimeEpoch)
            temp = hourly_data['temp']
            feelslike = hourly_data['feelslike']
            humidity = hourly_data['humidity']
            precip = hourly_data['precip']
            precipprob = hourly_data['precipprob']
            snow = hourly_data['snow']
            snowdepth = hourly_data['snowdepth']
            windgust = hourly_data['windgust']
            windspeed = hourly_data['windspeed']
            winddir = hourly_data['winddir']
            pressure = hourly_data['pressure']
            visibility = hourly_data['visibility']
            cloudcover = hourly_data['cloudcover']
            conditions = hourly_data['conditions']

            # Check if the data already exists in the table
            cursor.execute('SELECT datetimeEpoch FROM visualcrossing WHERE datetimeEpoch = ?', (datetimeEpoch,))
            existing_data = cursor.fetchone()

            if not existing_data:
                count += 1
                cursor.execute('''
                    INSERT INTO visualcrossing 
                    (datetimeEpoch, temp, feelslike, humidity, precip, precipprob, snow, snowdepth, windgust,
                    windspeed, winddir, pressure, visibility, cloudcover, conditions) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (datetimeEpoch, temp, feelslike, humidity, precip, precipprob, 
                    snow, snowdepth, windgust, windspeed, winddir, 
                    pressure, visibility, cloudcover, conditions))
                connection.commit()

cursor.execute('''
    SELECT COUNT(*) FROM visualcrossing
    ''')
rows = cursor.fetchone()[0]
print(rows)

connection.close()
