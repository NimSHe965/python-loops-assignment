#Task 1: Create an Array and Basic Math

import numpy as np

temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit using the formula (C * 1.8 + 32)
temps_fahrenheit = temps_celsius * 1.8 + 32

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

# Calculate the average temperature in Fahrenheit
avg_temp = np.mean(temps_fahrenheit)

# Round the average to 1 decimal place
avg_temp = round(avg_temp, 1)

print("Average Fahrenheit:", avg_temp)