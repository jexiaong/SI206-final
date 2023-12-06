import requests
import sqlite3
import sys

def cond_table(conn, cur, conditions):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS vc_conditions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conditions TEXT
            )
    ''')
    conn.commit()

    cur.execute('SELECT id FROM vc_conditions WHERE conditions = ?', (conditions,))
    existing_data = cursor.fetchone()
    if existing_data:
        return existing_data
    if not existing_data:
        cur.execute("INSERT INTO vc_conditions (conditions) VALUES (?)", (conditions,))
        conn.commit()

        cur.execute('SELECT id FROM vc_conditions WHERE conditions = ?', (conditions,))
        new_id = cur.fetchone()
        return new_id

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
            conditions INT
        )
    ''')
    conn.commit()

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=metric&key=DXM3T4BUXTSL3WQ47M2PKACHD&contentType=json")

if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()

jsonData = response.json()
# print(jsonData)

connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

#Create table if it doesn't already exist
create_table(connection, cursor)

count = 0
for day in jsonData['days']:
    for hourly_data in day['hours']:
        if count < 25:
            datetimeEpoch = hourly_data['datetimeEpoch']
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

                cond_id = cond_table(connection, cursor, conditions)[0]
                # print(cond_id)

                cursor.execute('''
                    INSERT INTO visualcrossing 
                    (datetimeEpoch, temp, feelslike, humidity, precip, precipprob, snow, snowdepth, windgust,
                    windspeed, winddir, pressure, visibility, cloudcover, conditions) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (datetimeEpoch, temp, feelslike, humidity, precip, precipprob, 
                    snow, snowdepth, windgust, windspeed, winddir, 
                    pressure, visibility, cloudcover, cond_id))
                connection.commit()

cursor.execute('''
    SELECT COUNT(*) FROM visualcrossing
    ''')
rows = cursor.fetchone()[0]
print(rows)

connection.close()
