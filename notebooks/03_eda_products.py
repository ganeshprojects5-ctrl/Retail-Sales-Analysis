import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the cleaned dataset
df = pd.read_csv('data/processed/sales_clean.csv')

# 2. Group by product description to find top 10 products by revenue
top_products_revenue = df.groupby('description')['revenue'].sum().reset_index()
top_products_revenue = top_products_revenue.sort_values(by='revenue', ascending=False).head(10)

# 3. Create a bar chart for Top 10 Products by Revenue
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products_revenue, x='revenue', y='description', palette='Blues_r')

# 4. Customize the chart labels
plt.title('Top 10 Products by Total Revenue', fontsize=14, fontweight='bold')
plt.xlabel('Total Revenue (£)', fontsize=12)
plt.ylabel('Product Description', fontsize=12)
plt.tight_layout()

# 5. Save the product chart into the outputs folder
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/top_products_revenue.png')
print("SUCCESS: top_products_revenue.png saved inside the outputs folder!")