#Task 2: Array Shape and Statistics

import numpy as np
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

shape_of_array = scores.shape
print("Shape:", shape_of_array)

total_elements = scores.size
print("Total elements:", total_elements)

# np.max() checks the whole array for the biggest number
highest_score = np.max(scores)
print("Highest score:", highest_score)

# np.min() checks the whole array for the smallest number
lowest_score = np.min(scores)
print("Lowest score:", lowest_score)

# The range is just the difference between the max and min
range_score = highest_score - lowest_score
print("Range:", range_score)