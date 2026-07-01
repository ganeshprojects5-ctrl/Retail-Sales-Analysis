import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the cleaned dataset
df = pd.read_csv('data/processed/sales_clean.csv')

# 2. Group by country to find top 5 countries by revenue (excluding United Kingdom if you want to see international sales, but let's keep all for now)
top_countries = df.groupby('country')['revenue'].sum().reset_index()
top_countries = top_countries.sort_values(by='revenue', ascending=False).head(5)

# 3. Create a bar chart for Top 5 Countries by Revenue
plt.figure(figsize=(10, 5))
sns.barplot(data=top_countries, x='revenue', y='country', palette='Greens_r')

# 4. Customize the chart labels
plt.title('Top 5 Countries by Total Revenue', fontsize=14, fontweight='bold')
plt.xlabel('Total Revenue (£)', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.tight_layout()

# 5. Save the country chart into the outputs folder
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/top_countries_revenue.png')
print("SUCCESS: top_countries_revenue.png saved inside the outputs folder!")