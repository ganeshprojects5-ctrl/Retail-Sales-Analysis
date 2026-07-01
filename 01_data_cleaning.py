import pandas as pd

# Raw data ni load cheyadam
# (Mee file peru 'online_retail.csv' lanti dhi edo okati ayyi undali)
df = pd.read_csv('data/raw/online_retail_II.csv', encoding='ISO-8859-1')

# Data entha peddadi undo chudadaniki
print("Data Shape (Rows, Columns):", df.shape)

# Modati 5 rows ni chudadaniki
print(df.head())
# 1. Column names ni standardized cheyadam (lowercase & underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 2. Cancellations ni remove cheyadam (Invoice numbers starting with 'C')
before_count = len(df)
df = df[~df['invoice'].astype(str).str.startswith('C')]

# 3. Valid sales mathrame unchadam (quantity > 0 mariyu price > 0)
df = df[(df['quantity'] > 0) & (df['price'] > 0)]

print(f"Valid sales rows: {len(df):,}")
print(f"Removed rows: {before_count - len(df):,}")
# 1. InvoiceDate ni proper datetime format ki marchadam
# 1. invoicedate ni proper datetime format ki marchadam (underscore lekunda)
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')

# 2. Revenue calculation
df['revenue'] = df['quantity'] * df['price']

# 3. Time features add cheyadam
df['year'] = df['invoicedate'].dt.year
df['month'] = df['invoicedate'].dt.month
df['year_month'] = df['invoicedate'].dt.to_period('M').astype(str)
df['day_of_week'] = df['invoicedate'].dt.day_name()
import os

# 'data/processed' ఫోల్డర్ క్రియేట్ చేయడం
os.makedirs('data/processed', exist_ok=True)

# డేటాని సేవ్ చేయడం
df.to_csv('data/processed/sales_clean.csv', index=False)
print("SUCCESS: sales_clean.csv file created successfully!")
# 'data/processed' ఫోల్డర్ క్రియేట్ చేయడం
os.makedirs('data/processed', exist_ok=True)

# డేటాని సేవ్ చేయడం
df.to_csv('data/processed/sales_clean.csv', index=False)
print("SUCCESS: sales_clean.csv file created successfully!")