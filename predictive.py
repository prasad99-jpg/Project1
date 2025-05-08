import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/prasad jadhav/Desktop/cpp.xlsx"
india_data = pd.read_excel(file_path, sheet_name="India")
china_data = pd.read_excel(file_path, sheet_name="China")

# Define the fields for prediction
fields_to_predict = ['Estimated population', 'Estimated deaths']

# Convert 'year' to datetime and set as index
india_data['year'] = pd.to_datetime(india_data['year'], format='%Y')
china_data['year'] = pd.to_datetime(china_data['year'], format='%Y')
india_data.set_index('year', inplace=True)
china_data.set_index('year', inplace=True)

# Ensure frequency is explicitly set
india_data = india_data.asfreq('YS')
china_data = china_data.asfreq('YS')

# Function to predict using ARIMA and plot
def predict_and_plot(data, column, country):
    # Train ARIMA model
    model = ARIMA(data[column], order=(1, 1, 1))  # You can tune ARIMA parameters
    model_fit = model.fit()

    # Predict for the next 3 years
    forecast = model_fit.get_forecast(steps=3)
    forecast_values = forecast.predicted_mean
    forecast_index = pd.date_range(start=data.index[-1] + pd.offsets.YearBegin(), periods=3, freq='YS')

    # Print predicted values
    print(f"Predictions for {column} in {country}:")
    for year, value in zip(forecast_index.year, forecast_values):
        print(f"  Year {year}: {value:.2f}")
    
    # Plot actual and predicted values
    plt.figure(figsize=(10, 6))
    plt.plot(data[column], label=f"{country} (Historical)", marker='o')
    plt.plot(forecast_index, forecast_values, label=f"{country} (Predicted)", marker='o', linestyle='--')
    plt.title(f"Prediction of {column} in {country} (2025-2027)")
    plt.xlabel("Year")
    plt.ylabel(column)
    plt.legend()
    plt.grid()
    plt.show()

# Predict for both India and China
for country, data in [('India', india_data), ('China', china_data)]:
    for column in fields_to_predict:
        predict_and_plot(data, column, country)