import matplotlib.pyplot as plt
import os

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split())) for line in lines]
    return zip(*data)

def average_vis():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = 'average.txt'
    file_path = os.path.join(current_directory, file_name)
    time, val = read_data(file_path)

    plt.plot(time, val, color='red', linestyle='dashed')

    plt.xlabel('Hourly Data since Collection Time')
    plt.ylabel('Average Wind Speed')
    plt.title('Comparing Average Difference in Wind Speed Between\nVisualcrossing API and WeatherApi Over Next 100 Hours')

    plt.savefig('avg_line.png')
    plt.close()

if __name__ == "__main__":
    average_vis()