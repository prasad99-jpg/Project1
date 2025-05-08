import pandas as pd
import statsmodels.api as sm
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the Excel database
excel_file = "C:/Users/prasad jadhav/Desktop/cpp.xlsx"

# Load data from specific sheet
def load_data(file_path, sheet_name):
    """Load data from the given Excel sheet."""
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Perform prescriptive analytics with visualizations
def perform_prescriptive_analytics_with_visualizations(df_india, df_china):
    """Analyze and visualize factors contributing to TB cases and deaths in India and China."""
    print("\n--- Prescriptive Analytics ---")
    
    # Combine data for comparison
    df_india['country'] = 'India'
    df_china['country'] = 'China'
    combined_df = pd.concat([df_india, df_china])

    # Regression analysis for India
    X_india = df_india[['Pct_healthcare in gdp', 'c_cdr', 'cfr']]
    y_india = df_india['estimated incidence cases']
    X_india = sm.add_constant(X_india)
    model_india = sm.OLS(y_india, X_india).fit()

    # Regression analysis for China
    X_china = df_china[['Pct_healthcare in gdp', 'c_cdr', 'cfr']]
    y_china = df_china['estimated incidence cases']
    X_china = sm.add_constant(X_china)
    model_china = sm.OLS(y_china, X_china).fit()

    # Display summaries
    print("\nIndia Model Summary:")
    print(model_india.summary())
    print("\nChina Model Summary:")
    print(model_china.summary())

    # Visualize comparisons of key metrics
    plt.figure(figsize=(12, 6))
    sns.barplot(data=combined_df.melt(id_vars=['country'], 
                                      value_vars=['Pct_healthcare in gdp', 'c_cdr', 'cfr']), 
                x='variable', y='value', hue='country')
    plt.title("Comparison of Key Metrics Between India and China")
    plt.ylabel("Value")
    plt.xlabel("Metrics")
    plt.legend(title="Country")
    plt.tight_layout()
    plt.show()

    # Visualize estimated TB cases and deaths
    plt.figure(figsize=(12, 6))
    sns.barplot(data=combined_df, x='country', y='estimated incidence cases', errorbar=None, hue='country', palette="viridis", dodge=False)

    plt.title("Estimated TB Cases in India vs China")
    plt.ylabel("Estimated Cases")
    plt.xlabel("Country")
    plt.tight_layout()
    plt.show()

    # Mean comparison and recommendations
    india_means = df_india[['Pct_healthcare in gdp', 'c_cdr', 'cfr', 'estimated incidence cases']].mean()
    china_means = df_china[['Pct_healthcare in gdp', 'c_cdr', 'cfr', 'estimated incidence cases']].mean()

    print("\n--- Mean Comparison ---")
    print("India Means:\n", india_means)
    print("China Means:\n", china_means)

    print("\n--- Recommendations ---")
    if india_means['Pct_healthcare in gdp'] < china_means['Pct_healthcare in gdp']:
        print("Increase healthcare spending as a percentage of GDP.")
    if india_means['c_cdr'] < china_means['c_cdr']:
        print("Improve case detection rate (c_cdr).")
    if india_means['cfr'] > china_means['cfr']:
        print("Focus on reducing case fatality ratio (cfr).")

    
# Monitor changes in the Excel file
def monitor_changes_with_visualizations(file_path, sheet_names, interval=60):
    """Monitor Excel sheets for changes and re-run analytics with visualizations if changes are detected."""
    print("\nStarting monitoring framework...")
    prev_data = {sheet: None for sheet in sheet_names}

    while True:
        changes_detected = False

        for sheet in sheet_names:
            current_data = load_data(file_path, sheet)
            
            # Check if data has changed for the current sheet
            if prev_data[sheet] is None or not current_data.equals(prev_data[sheet]):
                print(f"\nChanges detected in sheet: {sheet}")
                prev_data[sheet] = current_data
                changes_detected = True

        # If changes are detected, re-run the analytics with visualizations
        if changes_detected:
            print("\nRe-running prescriptive analytics with visualizations...")
            india_data = prev_data.get("India")
            china_data = prev_data.get("China")
            if india_data is not None and china_data is not None:
                perform_prescriptive_analytics_with_visualizations(india_data, china_data)

        # Wait before the next check
        time.sleep(interval)

# Run the framework
if __name__ == "__main__":
    try:
        sheet_names = ["India", "China"]
        monitor_changes_with_visualizations(excel_file, sheet_names, interval=60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")