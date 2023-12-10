import matplotlib.pyplot as plt
import os

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split())) for line in lines]
    return zip(*data)

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'average.txt'
file_path = os.path.join(current_directory, file_name)
time, val = read_data(file_path)

plt.plot(time, val, color='red')

plt.xlabel('Hourly Data since 12/9/2023')
plt.ylabel('Average Wind Speed')
plt.title('Comparing Average Difference in Wind Speed Between\nVisualcrossing API and WeatherApi Over 100 Hours since 12/9/2023')

plt.savefig('avg_line.png')
plt.close()