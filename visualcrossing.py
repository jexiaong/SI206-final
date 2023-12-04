import requests
import sqlite3
import sys

# Function to create SQLite table
def create_table():
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visualcrossing.py (
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
            UNIQUE(location, timestamp)
        )
    ''')

    connection.commit()
    connection.close()

# Function to insert data into the SQLite table
def insert_data(location, timestamp, temperature, precipitation):
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    # Check if the data already exists in the table
    cursor.execute('SELECT id FROM weather WHERE location = ? AND timestamp = ?', (location, timestamp))
    existing_data = cursor.fetchone()

    if not existing_data:
        # Insert data into the 'weather' table
        cursor.execute('INSERT INTO weather (location, timestamp, temperature, precipitation) VALUES (?, ?, ?, ?)',
                       (location, timestamp, temperature, precipitation))
        connection.commit()
        print(f'Data for {location} at {timestamp} inserted successfully.')
    else:
        print(f'Data for {location} at {timestamp} already exists in the database.')

    connection.close()

# Make the GET request
response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Ann%20Arbor%2C%20Michigan?unitGroup=metric&include=hours&key=DXM3T4BUXTSL3WQ47M2PKACHD&contentType=json")

# Check if the request was successful (status code 200)
if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()

# Parse the JSON response
jsonData = response.json()

# Create the SQLite table if it doesn't exist
create_table()

# Extract relevant data from the JSON and insert into the database
for hourly_data in jsonData['hours']:
    timestamp = hourly_data['datetime']
    temperature = hourly_data['temp2m']
    precipitation = hourly_data['precip']

    # Replace 'Ann Arbor, Michigan' with the actual location
    insert_data('Ann Arbor, Michigan', timestamp, temperature, precipitation)
