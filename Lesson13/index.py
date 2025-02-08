import numpy as np
import pandas as pd

# 2D Array Example
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2D Array:")
print(arr_2d)

element = arr_2d[1, 2]
print("\nElement at position [1,2]:", element)

# Sales Data
product = ['apple', 'oranges', 'tangerine', 'pears']
sales = [150, 200, 350.90, 100]  # Sales values
sales_series = pd.Series(sales, index=product)

print("\nSales Series:")
print(sales_series)

# Calculate Total Sales
total_sales = sales_series.sum()
print("\nTotal Sales:", total_sales)

# Add a new product and update the sales
sales_series['bananas'] = 300
print("\nUpdated Sales Series with Bananas:")
print(sales_series)

# Calculate average sales per product
average_sales = sales_series.mean()
print("\nAverage Sales per Product:", average_sales)

# More NumPy array manipulation
arr_1d = np.array([10, 20, 30, 40, 50])

# Sum of elements in 1D array
sum_arr = arr_1d.sum()
print("\nSum of elements in arr_1d:", sum_arr)

# Perform element-wise multiplication of 2D and 1D arrays (broadcasting)
result = arr_2d * arr_1d[:5]
print("\nElement-wise multiplication of 2D and 1D arrays (broadcasting):")
print(result)

# Generate random numbers
random_array = np.random.rand(3, 3)  # 3x3 matrix of random numbers between 0 and 1
print("\nRandom 3x3 Array:")
print(random_array)

# Calculate the mean of the random array
random_mean = random_array.mean()
print("\nMean of the random array:", random_mean)

# Sorting and Indexing
sorted_sales = sales_series.sort_values(ascending=False)
print("\nSorted Sales (Descending):")
print(sorted_sales)

# Filter products with sales greater than 150
filtered_sales = sales_series[sales_series > 150]
print("\nProducts with Sales > 150:")
print(filtered_sales)
