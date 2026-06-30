import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the cleaned dataset
df = pd.read_csv('data/processed/sales_clean.csv')

# 2. Group data by month and calculate total revenue
monthly_sales = df.groupby('year_month')['revenue'].sum().reset_index()

# 3. Create the trend plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='year_month', y='revenue', marker='o', color='b')

# 4. Customize the chart labels
plt.title('Monthly Sales Revenue Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month (Year-Month)', fontsize=12)
plt.ylabel('Total Revenue (£)', fontsize=12)
plt.xticks(rotation=45) # Rotates the dates so they don't overlap
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 5. Create an output folder for plots and save the chart
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/monthly_sales_trend.png')
print("SUCCESS: monthly_sales_trend.png saved inside the outputs folder!")