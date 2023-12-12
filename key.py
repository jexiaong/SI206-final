import sqlite3

def key():
    conn = sqlite3.connect('weather_data.db')
    cur = conn.cursor()

    cur.execute('SELECT MIN(hours) FROM visualcrossing')
    lowest_time_epoch = cur.fetchone()[0]

    cur.execute('SELECT hours FROM visualcrossing')
    for row in cur.fetchall():
        time_since_lowest_epoch = (row[0] - lowest_time_epoch) // 3600

        #update primary key
        cur.execute('UPDATE visualcrossing SET hours = ? WHERE hours = ?', (time_since_lowest_epoch, row[0]))

    cur.execute('SELECT hours FROM weatherapi')
    for row in cur.fetchall():
        time_since_lowest_epoch = (row[0] - lowest_time_epoch) // 3600

        #update primary key
        cur.execute('UPDATE weatherapi SET hours = ? WHERE hours = ?', (time_since_lowest_epoch, row[0]))
    conn.commit()

if __name__ == "__main__":
    key()
