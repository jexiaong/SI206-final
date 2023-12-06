import requests
import sqlite3
import sys

def create_table():
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visualcrossing (
            datetime INTEGER PRIMARY KEY,
            temp REAL,
            feelslike REAL,
            humidity REAL,
            precip TEXT,
            precipprob REAL,
            snow TEXT,
            snowdepth REAL,
            preciptype TEXT,
            windgust REAL,
            windspeed REAL,
            winddir REAL,
            pressure REAL,
            visibility REAL,
            cloudcover REAL,
            conditions TEXT,
            UNIQUE(datetime,)
        )
    ''')

    connection.commit()
    connection.close()

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Ann%20Arbor%2C%20Michigan?unitGroup=metric&include=hours&key=DXM3T4BUXTSL3WQ47M2PKACHD&contentType=json")

if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()

jsonData = response.json()

#Create table if it doesn't already exist
create_table()

for hourly_data in jsonData['hours']:
    datetime = hourly_data['datetime']
    temp = hourly_data['temp']
    feelslike = hourly_data['feelslike']
    humidity = hourly_data['humidity']
    precip = hourly_data['precip']
    precipprob = hourly_data['precipprob']
    snow = hourly_data['snow']
    snowdepth = hourly_data['snowdepth']
    preciptype = hourly_data['preciptype']
    windgust = hourly_data['windgust']
    windspeed = hourly_data['windspeed']
    winddir = hourly_data['datetwinddirime']
    pressure = hourly_data['pressure']
    visibility = hourly_data['visibility']
    cloudcover = hourly_data['cloudcover']
    conditions = hourly_data['conditions']

    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    # Check if the data already exists in the table
    cursor.execute('SELECT datetime FROM weather WHERE datetime = ?', (datetime,))
    existing_data = cursor.fetchone()

    if not existing_data:
        cursor.execute('''
                       INSERT INTO weather (datetime, temp, feelslike, humidity, 
                       precip, precipprob, snow, snowdepth, preciptype, windgust,
                       windspeed, winddir, pressure, visibility, cloudcover, conditions) 
                       VALUES (?, ?, ?, ?)
                       ''',
                       (location, timestamp, temperature, precipitation))
        connection.commit()
        print(f'Data for {location} at {timestamp} inserted successfully.')
    else:
        print(f'Data for {location} at {timestamp} already exists in the database.')

    connection.close()
