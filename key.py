import sqlite3

def key():
    conn = sqlite3.connect('weather_data.db')
    cur = conn.cursor()

    cur.execute('SELECT MIN(datetimeEpoch) FROM visualcrossing')
    lowest_time_epoch = cur.fetchone()[0]

    cur.execute('SELECT datetimeEpoch FROM visualcrossing')
    for row in cur.fetchall():
        time_since_lowest_epoch = (row[0] - lowest_time_epoch) // 3600

        #update primary key
        cur.execute('UPDATE visualcrossing SET datetimeEpoch = ? WHERE datetimeEpoch = ?', (time_since_lowest_epoch, row[0]))

    cur.execute('SELECT time_epoch FROM weatherapi')
    for row in cur.fetchall():
        time_since_lowest_epoch = (row[0] - lowest_time_epoch) // 3600

        #update primary key
        cur.execute('UPDATE weatherapi SET time_epoch = ? WHERE time_epoch = ?', (time_since_lowest_epoch, row[0]))
    conn.commit()

if __name__ == "__main__":
    key()
