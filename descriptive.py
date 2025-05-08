#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
file_path = "C:/Users/prasad jadhav/Desktop/cpp.xlsx"  # Replace with your actual file path
india_data = pd.read_excel(file_path, sheet_name="India")  # India sheet
china_data = pd.read_excel(file_path, sheet_name="China")  # China sheet

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(india_data['year'], india_data['estimated incidence cases'], label='India', marker='o', color='blue')
plt.plot(china_data['year'], china_data['estimated incidence cases'], label='China', marker='o', color='red')

# Add titles and labels
plt.title("Comparison of Estimated Incidence Cases Between India and China", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Estimated Incidence Cases", fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()