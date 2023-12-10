import sqlite3
connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()
cursor.execute('''
    SELECT vc.datetimeEpoch, vc.windspeed, wa.wind_kph
    FROM visualcrossing AS vc
    JOIN weatherapi AS wa ON vc.datetimeEpoch = wa.time_epoch;
    ''')
result = cursor.fetchall()
avg_list = []
for entry in result:
    avg = (entry[1]+entry[2])/2
    avg_list.append((entry[0], avg))
print(avg_list)
avg_list = sorted(avg_list, key=lambda x: x[0])
file_path = 'average.txt'
i = 0
with open(file_path, 'w') as file:
    for item in avg_list:
        file.write(f"{i}\t{item[1]}\n")
        i += 1