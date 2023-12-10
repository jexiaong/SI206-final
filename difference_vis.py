# import seaborn as sns
# import os
# import matplotlib.pyplot as plt

# def read_data(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         data = [list(map(float, line.strip().split())) for line in lines]
#     return zip(*data)

# current_directory = os.path.dirname(os.path.abspath(__file__))
# file_name = 'difference.txt'
# file_path = os.path.join(current_directory, file_name)
# time, vs, wa = read_data(file_path)

# # Set the Seaborn style
# sns.set(style="whitegrid")

# # Plot using Seaborn
# plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
# sns.lineplot(x=time, y=vs, label='Line 1')
# sns.lineplot(x=time, y=wa, label='Line 2')

# plt.xlabel('Hourly Data since 12/9/2023')
# plt.ylabel('Difference in Perceived and Actual Temperatures')
# plt.title('Comparing Difference in Perceived and Actual Temperature Data\nBetween Visualcrossing API and WeatherApi over 100 Hours Since 12/9/2023')
# plt.legend()

# plt.savefig('difference.png')

import seaborn as sns
import os
import matplotlib.pyplot as plt

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split())) for line in lines]
    return zip(*data)

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'difference.txt'
file_path = os.path.join(current_directory, file_name)
time, vs, wa = read_data(file_path)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=time, y=vs, label='Line 1', color='green', marker='s')
sns.scatterplot(x=time, y=wa, label='Line 2', color='orange')

plt.xlabel('Hourly Data since 12/9/2023')
plt.ylabel('Difference in Perceived and Actual Temperatures')
plt.title('Comparing Difference in Perceived and Actual Temperature Data\nBetween Visualcrossing API and WeatherApi over 100 Hours Since 12/9/2023')
plt.legend()

plt.savefig('difference_scatter.png')
plt.close()
