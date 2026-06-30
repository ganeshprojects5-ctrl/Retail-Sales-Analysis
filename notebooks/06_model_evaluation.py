import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error
import os

# 1. Load and prepare historical daily data
df = pd.read_csv('data/processed/sales_clean.csv')
df['invoicedate'] = pd.to_datetime(df['invoicedate'])
df['invoice_day'] = df['invoicedate'].dt.date
daily_data = df.groupby('invoice_day')['revenue'].sum().reset_index()
daily_data.columns = ['ds', 'y']

# 2. Train the model
model = Prophet(yearly_seasonality=True, daily_seasonality=False)
model.fit(daily_data)

# 3. Predict on the historical dates to see how well it fits
forecast = model.predict(daily_data)

# 4. Calculate the Mean Absolute Error (MAE)
actuals = daily_data['y']
predictions = forecast['yhat']
mae = mean_absolute_error(actuals, predictions)

print("\n====================================")
print(f"Model Mean Absolute Error (MAE): £{mae:.2f}")
print("====================================")
print("This means on any given day, the model's prediction is off by roughly this amount.")