import sqlite3

connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()
cursor.execute('''
    SELECT vc.datetimeEpoch, vc.temp, vc.feelslike, wa.temp_c, wa.feelslike_c
    FROM visualcrossing AS vc
    JOIN weatherapi AS wa ON vc.datetimeEpoch = wa.time_epoch;
    ''')
result = cursor.fetchall()
print(result)

data = []
for r in result:
    vc_diff = abs(r[1] - r[2])
    wa_diff = abs(r[3] - r[4])
    data.append((r[0], vc_diff, wa_diff))

file_path = 'difference.txt'
with open(file_path, 'w') as file:
    for d in data:
        file.write(f"Time Epoch: {d[0]}\tVisualcrossing difference: {d[1]}\tWeatherapi difference: {d[2]}\n")