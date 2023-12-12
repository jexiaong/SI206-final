import sqlite3

def avg_wind():
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT vc.hours, vc.windspeed, wa.wind_kph
        FROM visualcrossing AS vc
        JOIN weatherapi AS wa ON vc.hours = wa.hours;
        ''')
    result = cursor.fetchall()
    avg_list = []
    for entry in result:
        avg = (entry[1]+entry[2])/2
        avg_list.append((entry[0], avg))
    print(avg_list)
    avg_list = sorted(avg_list, key=lambda x: x[0])
    file_path = 'average.txt'
    with open(file_path, 'w') as file:
        file.write("hours\taverage difference in windspeed\n")
        for item in avg_list:
            file.write(f"{item[0]}\t{item[1]}\n")

if __name__ == "__main__":
    avg_wind()