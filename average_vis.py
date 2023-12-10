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

plt.plot(time, val)

plt.xlabel('Hourly Data')
plt.ylabel('Average Wind Speed')
plt.title('Line Graph showing hourly variations in average wind speed')
plt.legend()

# Show the plot
plt.show()