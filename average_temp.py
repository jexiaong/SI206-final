import sqlite3

connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()
cursor.execute('''
    SELECT vc.datetimeEpoch, vc.temp, wa.temp_c
    FROM visualcrossing AS vc
    JOIN weatherapi AS wa ON vc.datetimeEpoch = wa.time_epoch;
    ''')
result = cursor.fetchall()