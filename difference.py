import sqlite3

def difference():
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT vc.hours, vc.temp, vc.feelslike, wa.temp_c, wa.feelslike_c
        FROM visualcrossing AS vc
        JOIN weatherapi AS wa ON vc.hours = wa.hours;
        ''')
    result = cursor.fetchall()
    print(result)

    data = []
    for r in result:
        vc_diff = abs(r[1] - r[2])
        wa_diff = abs(r[3] - r[4])
        data.append((r[0], vc_diff, wa_diff))

    data = sorted(data, key=lambda x: x[0])

    file_path = 'difference.txt'
    with open(file_path, 'w') as file:
        file.write("hours\tvisualcrossing difference\tweatherapi difference\n")
        for d in data:
            file.write(f"{d[0]}\t{d[1]}\t{d[2]}\n")

if __name__ == "__main__":
    difference()