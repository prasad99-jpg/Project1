import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from the Excel file
file_path = "C:/Users/prasad jadhav/Desktop/cpp.xlsx"  # Replace with your actual file path
india_data = pd.read_excel(file_path, sheet_name="India")  # India sheet
china_data = pd.read_excel(file_path, sheet_name="China")  # China sheet

# Combine the datasets for easier comparison
india_data['country'] = 'India'
china_data['country'] = 'China'
combined_data = pd.concat([india_data, china_data])

# Diagnostic Analytics: Key Comparisons
# 1. Descriptive Statistics for Key Fields
fields_to_analyze = [
    'Pct_healthcare in gdp',
    'c_cdr',
    'cfr',
    'estimated prevalence of all TB forms',
    'estimated_mortality of HIV-Positive(100k)',
]
for field in fields_to_analyze:
    print(f"\n{field} - Descriptive Statistics")
    print(combined_data.groupby('country')[field].describe())

# 2. Correlation Analysis
correlation_matrix = combined_data[[
    'Pct_healthcare in gdp', 'c_cdr', 'cfr', 
    'estimated prevalence of all TB forms', 
    'estimated_mortality of HIV-Positive(100k)', 
    'estimated incidence cases'
]].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Matrix for Contributing Factors")
plt.show()

# 3. Line Chart Comparison for Estimated Incidence Cases
plt.figure(figsize=(10, 6))
sns.lineplot(data=combined_data, x='year', y='estimated incidence cases', hue='country', marker='o')
plt.title("Comparison of Estimated Incidence Cases Between India and China")
plt.xlabel("Year")
plt.ylabel("Estimated Incidence Cases")
plt.grid(True)
plt.legend(title="Country")
plt.show()

# 4. Visualizing Key Contributing Factors Over Time
for field in fields_to_analyze:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=combined_data, x='year', y=field, hue='country', marker='o')
    plt.title(f"Comparison of {field} Between India and China Over Time")
    plt.xlabel("Year")
    plt.ylabel(field)
    plt.grid(True)
    plt.legend(title="Country")
    plt.show()