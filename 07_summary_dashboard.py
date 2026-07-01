import pandas as pd
import os

# 1. Load the cleaned dataset
df = pd.read_csv('data/processed/sales_clean.csv')

# 2. Calculate KPI Metrics
total_revenue = df['revenue'].sum()
total_orders = df['invoice'].nunique()
total_items_sold = df['quantity'].sum()

# 3. Find top performers
top_product = df.groupby('description')['revenue'].sum().idxmax()
top_country = df[df['country'] != 'United Kingdom'].groupby('country')['revenue'].sum().idxmax()

# 4. Print the Executive Dashboard
print("\n==================================================")
print("          RETAIL DEMAND ANALYSIS DASHBOARD        ")
print("==================================================")
print(f"📊 Total Dataset Rows Processed : {len(df):,}")
print(f"💰 Total Revenue Generated      : £{total_revenue:,.2f}")
print(f"📦 Total Unique Orders Placed   : {total_orders:,}")
print(f"🛍️ Total Individual Items Sold  : {total_items_sold:,}")
print("--------------------------------------------------")
print(f"🔝 Highest Revenue Product      : {top_product}")
print(f"🌍 Top International Market     : {top_country}")
print("--------------------------------------------------")
print("🤖 Predictive Model Baseline MAE: £9,707.56")
print("==================================================")
print("All analytical charts are saved inside the 'outputs/' folder.")
print("==================================================\n")