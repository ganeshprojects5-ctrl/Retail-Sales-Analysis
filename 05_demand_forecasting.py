import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

# 1. Load and clean data structure
df = pd.read_csv('data/processed/sales_clean.csv')
df['invoicedate'] = pd.to_datetime(df['invoicedate'])
df['invoice_day'] = df['invoicedate'].dt.date

# 2. Aggregate daily revenue
daily_data = df.groupby('invoice_day')['revenue'].sum().reset_index()
daily_data.columns = ['ds', 'y']

# 3. Initialize and train the Prophet model
model = Prophet(yearly_seasonality=True, daily_seasonality=False)
model.fit(daily_data)

# 4. Create a placeholder dataframe for 30 days into the future
future = model.make_future_dataframe(periods=30)

# 5. Predict the future demand
forecast = model.predict(future)

# 6. Plot the forecast results and save the image
fig = model.plot(forecast)
plt.title('30-Day Revenue Demand Forecast', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Revenue (£)', fontsize=12)

os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/demand_forecast.png')
print("SUCCESS: demand_forecast.png saved inside the outputs folder!")
# 7. Plot the components (trend, weekly, yearly seasonality) and save
fig2 = model.plot_components(forecast)
plt.tight_layout()
plt.savefig('outputs/forecast_components.png')
print("SUCCESS: forecast_components.png saved inside the outputs folder!")