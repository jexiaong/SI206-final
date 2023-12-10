import matplotlib.pyplot as plt
import os

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split())) for line in lines]
    return zip(*data)

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'difference.txt'
file_path = os.path.join(current_directory, file_name)
time, vs, wa = read_data(file_path)

# Create a plot with two line graphs
plt.plot(time, vs, label='Line 1')
plt.plot(time, wa, label='Line 2')

# Add labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Line Graphs')
plt.legend()

# Show the plot
plt.show()
