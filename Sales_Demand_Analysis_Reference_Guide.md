# Sales & Demand Analysis — End-to-End Project Reference Guide
### EDA + Business Insights with Python, SQL, and Power BI

This is a complete, build-it-yourself reference. It takes you from a raw sales file all the way to a polished Power BI dashboard and a written set of business recommendations. Work through it phase by phase. Every phase explains *what* you are doing, *why* it matters, and gives you *real, runnable* code you can adapt.

---

## Table of Contents

1. [Project Overview & Objectives](#1-project-overview--objectives)
2. [Tech Stack & Why Each Tool](#2-tech-stack--why-each-tool)
3. [Project Folder Structure](#3-project-folder-structure)
4. [Environment Setup](#4-environment-setup)
5. [Phase 0 — Data Understanding](#5-phase-0--data-understanding)
6. [Phase 1 — Load & First Look (Python)](#6-phase-1--load--first-look-python)
7. [Phase 2 — Data Cleaning (Python)](#7-phase-2--data-cleaning-python)
8. [Phase 3 — Exploratory Data Analysis (Python + Matplotlib)](#8-phase-3--exploratory-data-analysis-python--matplotlib)
9. [Phase 4 — SQL Analysis](#9-phase-4--sql-analysis)
10. [Phase 5 — Power BI Dashboard](#10-phase-5--power-bi-dashboard)
11. [Phase 6 — Business Insights](#11-phase-6--business-insights)
12. [Phase 7 — Conclusions, Documentation & Portfolio Write-up](#12-phase-7--conclusions-documentation--portfolio-write-up)
13. [Appendix A — Project Checklist](#appendix-a--project-checklist)
14. [Appendix B — Suggested Timeline](#appendix-b--suggested-timeline)
15. [Appendix C — Common Pitfalls](#appendix-c--common-pitfalls)
16. [Appendix D — Stretch Goals](#appendix-d--stretch-goals)
17. [Appendix E — Resources](#appendix-e--resources)

---

## 1. Project Overview & Objectives

### The business problem
A retailer (or e-commerce store) wants to understand its sales performance to make better decisions about **inventory, marketing, and product range**. They have transaction-level sales data but no clear view of *what sells, when it sells, and which products actually drive the money*.

Your job as the analyst is to turn that raw transaction log into clear answers and recommendations.

### What you will deliver (the four key outputs)

| # | Output | The question it answers |
|---|--------|--------------------------|
| 1 | **Demand trends** | Is demand growing, flat, or declining over time? |
| 2 | **Top & bottom products** | Which products should we stock more of, and which should we drop? |
| 3 | **Seasonal spikes** | When in the year/week does demand peak, so we can plan ahead? |
| 4 | **Revenue contribution analysis** | Which products/categories actually generate most of the revenue? |

### Skills this project demonstrates (good for a portfolio / CV)
- **Data wrangling** — cleaning messy real-world transaction data with Pandas.
- **EDA & visualization** — finding and communicating patterns with Matplotlib.
- **SQL** — aggregation, window functions, CTEs, time-series queries.
- **BI / dashboarding** — data modelling, DAX, and interactive reporting in Power BI.
- **Business storytelling** — translating numbers into recommendations.

### Definition of "done"
By the end you will have:
- A cleaned dataset (`sales_clean.csv`) and a documented cleaning process.
- A Jupyter notebook of EDA with labelled charts.
- A `.sql` file of analysis queries that reproduce the key outputs.
- A multi-page Power BI dashboard (`.pbix`).
- A short written report / README with insights and recommendations.

---

## 2. Tech Stack & Why Each Tool

| Tool | Role in this project | Why it's used here |
|------|----------------------|--------------------|
| **Python (Pandas)** | Cleaning + reshaping data | Handles messy data and large transformations far faster than spreadsheets. |
| **Python (Matplotlib)** | EDA charts | Lets you explore patterns quickly and reproducibly before committing to a dashboard. |
| **SQL** | Aggregated analysis | The industry-standard language for querying data; shows you can answer questions directly against a database. |
| **Power BI** | Interactive dashboard | Where stakeholders actually *consume* the analysis — filters, drill-downs, KPIs. |

**How the tools connect (the data flow):**

```
Raw file (CSV/Excel)
        │
        ▼
[Python + Pandas]  →  clean, validate, engineer columns
        │
        ├─────────────► sales_clean.csv ──────────► [Power BI] (import & model)
        │
        ▼
[Load into a database]  →  [SQL] aggregated analysis & validation
```

You clean once in Python, then feed the clean output into **both** SQL (for query-based analysis) and Power BI (for the dashboard). Doing the heavy cleaning once, upstream, keeps everything consistent.

---

## 3. Project Folder Structure

Set this up first. A tidy structure makes the project reproducible and looks professional on GitHub.

```
sales-demand-analysis/
├── data/
│   ├── raw/                  # original, untouched downloaded file(s)
│   │   └── online_retail.csv
│   └── processed/
│       └── sales_clean.csv   # output of your cleaning step
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda.ipynb
├── sql/
│   ├── 00_create_table.sql
│   └── 01_analysis_queries.sql
├── powerbi/
│   └── sales_dashboard.pbix
├── reports/
│   ├── figures/              # exported charts (.png)
│   └── insights.md           # final written findings
├── requirements.txt
└── README.md
```

> **Rule of thumb:** never edit files in `data/raw/`. Treat them as read-only originals so you can always reproduce your work from scratch.

---

## 4. Environment Setup

### 4.1 Install Python & libraries
Install [Anaconda](https://www.anaconda.com/download) (easiest — comes with Jupyter and most libraries) **or** plain Python 3.10+.

Create `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn          # optional, for nicer heatmaps
jupyter
sqlalchemy       # to write a DataFrame into a database
openpyxl         # to read .xlsx files
statsmodels      # optional, for seasonal decomposition
```

Install everything:

```bash
# (optional) create an isolated environment first
python -m venv venv
# Windows: venv\Scripts\activate     |     Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
```

### 4.2 Install a database engine for the SQL phase
Pick **one**:

- **Easiest, zero-setup — SQLite.** No server to install. Use the free [DB Browser for SQLite](https://sqlitebrowser.org/) GUI to run queries. You can create the database directly from Python.
- **Most "resume-friendly" — PostgreSQL.** Install [PostgreSQL](https://www.postgresql.org/download/) + the free [pgAdmin](https://www.pgadmin.org/) or [DBeaver](https://dbeaver.io/) client. Power BI connects to it natively. This guide's SQL is written for PostgreSQL, with SQLite differences flagged.
- **A middle path — DuckDB.** Reads CSVs directly with full SQL and no server. Great if you just want SQL practice without loading a database.

> **Recommendation for a first project:** use **SQLite** for the SQL phase (fastest to get going) and import a **CSV** into Power BI. Once comfortable, redo it with PostgreSQL to show off a real database connection.

### 4.3 Install Power BI
Download the free [**Power BI Desktop**](https://www.microsoft.com/power-platform/products/power-bi/desktop) (Windows only). If you're on Mac/Linux, options are a Windows VM, or build the equivalent dashboard in **Tableau Public** (free) and note the substitution in your write-up.

---

## 5. Phase 0 — Data Understanding

Before writing any code, understand what data you have. This phase is about *getting the right dataset and knowing its columns*.

### 5.1 Choose a dataset
You need transaction-level sales data: ideally one row per item sold, with a **date**, a **product**, a **quantity**, and a **price** (or a revenue/sales amount). Two excellent free options:

**Option A — Online Retail II (recommended for showing cleaning skills)**
- Source: UCI Machine Learning Repository / Kaggle ("Online Retail II"). Search: *"Online Retail II UCI"*.
- Real UK e-commerce, ~1M rows across ~2 years. It is *deliberately messy* (cancellations, negative quantities, missing customer IDs) — perfect for demonstrating data-cleaning skills, and it has a strong December seasonal spike.
- Columns: `Invoice`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `Price`, `Customer ID`, `Country`.

**Option B — Sample Superstore (recommended if you want a smoother ride)**
- Source: widely available on Kaggle ("Superstore dataset"). Search: *"Sample Superstore"*.
- ~10k rows, already fairly clean, and includes `Category`, `Sub-Category`, `Region`, `Sales`, `Profit` — great for revenue/category breakdowns and maps.
- Columns include: `Order Date`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Profit`, `Region`, `Segment`.

> This guide's **code is written against the Online Retail schema** (the messier, more instructive case). If you use Superstore, you can **skip the cancellation/negative-value cleaning** and **map column names** using the table below.

### 5.2 Standard "analysis schema" used in this guide
To keep everything consistent, we'll work toward these standardized columns after cleaning:

| Standard column | Meaning | Online Retail source | Superstore source |
|-----------------|---------|----------------------|-------------------|
| `invoice` | Order / transaction ID | `Invoice` | `Order ID` |
| `stock_code` | Product code | `StockCode` | `Product ID` |
| `description` | Product name | `Description` | `Product Name` |
| `quantity` | Units sold | `Quantity` | `Quantity` |
| `price` | Unit price | `Price` | *(derive: `Sales`/`Quantity`)* |
| `revenue` | quantity × price | *(derive)* | `Sales` |
| `invoice_date` | Date of sale | `InvoiceDate` | `Order Date` |
| `country` / `region` | Geography | `Country` | `Region` |
| `customer_id` | Customer | `Customer ID` | `Customer ID` |
| `category` | Product category | *(not present)* | `Category` |

### 5.3 Write a quick data dictionary
In your README, note: how many rows/columns, the date range, the grain (one row = one product line on one invoice), and any known quirks. You'll confirm these numbers in Phase 1. This habit signals analytical maturity.

---

## 6. Phase 1 — Load & First Look (Python)

Goal: load the data and form a first impression — size, types, missingness, obvious problems. Do this in `notebooks/01_data_cleaning.ipynb`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)   # see all columns
pd.set_option('display.float_format', '{:,.2f}'.format)

# --- Load ---
# CSV version:
df = pd.read_csv('../data/raw/online_retail.csv', encoding='ISO-8859-1')
# If you have the Excel version instead:
# df = pd.read_excel('../data/raw/online_retail_II.xlsx', sheet_name=0)

print(df.shape)        # (rows, columns)
df.head(10)
```

> **Why `encoding='ISO-8859-1'`?** This dataset contains non-UTF-8 characters in product descriptions; the default UTF-8 reader will error. This is a common real-world gotcha.

### 6.1 Inspect structure and quality

```python
df.info()              # column names, non-null counts, dtypes
df.describe()          # summary stats for numeric columns — watch for negatives/outliers
df.isnull().sum()      # missing values per column
df.duplicated().sum()  # exact duplicate rows
df.nunique()           # unique values per column (e.g., how many products, customers)
```

### 6.2 Things to actively look for
- **Date range:** `df['InvoiceDate'].min(), df['InvoiceDate'].max()` — confirm the period.
- **Negative or zero `Quantity`/`Price`:** returns, cancellations, or data errors.
- **Missing `Customer ID`:** common in this dataset (guest checkouts / data gaps).
- **Cancellation invoices:** in Online Retail, invoices starting with the letter **`C`** are cancellations.
- **Suspicious `StockCode`s:** non-product codes like `POST` (postage), `BANK CHARGES`, `M` (manual), `D` (discount).

```python
# Quick diagnostics
print("Negative quantity rows:", (df['Quantity'] < 0).sum())
print("Zero/negative price rows:", (df['Price'] <= 0).sum())
print("Cancellation invoices:", df['Invoice'].astype(str).str.startswith('C').sum())
print("Missing Customer ID:", df['Customer ID'].isnull().sum())
```

Write down what you find — these notes become your cleaning plan.

---

## 7. Phase 2 — Data Cleaning (Python)

Goal: produce a trustworthy `sales_clean.csv`. **Clean deliberately and document every decision** — in a real job, someone will ask "why did you drop those rows?"

> For **demand and revenue** analysis we keep *all valid sales* (we do **not** need a customer ID for product-level demand), but we remove cancellations, returns, and junk rows so totals are accurate. If you later add a customer-segmentation section, you would then drop missing customer IDs.

### 7.1 Standardize column names
Makes code cleaner and avoids spaces/case issues.

```python
df.columns = (df.columns
              .str.strip()
              .str.lower()
              .str.replace(' ', '_'))
# Online Retail II -> 'customer_id' (handles the space in 'Customer ID')
df.head()
```

### 7.2 Parse dates

```python
df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
print("Rows with unparseable date:", df['invoice_date'].isnull().sum())
print("Date range:", df['invoice_date'].min(), "→", df['invoice_date'].max())
```

### 7.3 Remove cancellations and returns

```python
# Drop cancellation invoices (start with 'C')
before = len(df)
df = df[~df['invoice'].astype(str).str.startswith('C')]

# Keep only genuine sales: positive quantity and positive price
df = df[(df['quantity'] > 0) & (df['price'] > 0)]

print(f"Removed {before - len(df):,} cancellation/invalid rows")
```

### 7.4 Remove non-product / junk stock codes (Online Retail specific)

```python
# These codes are charges/adjustments, not products
junk_codes = ['POST', 'DOT', 'C2', 'BANK CHARGES', 'M', 'AMAZONFEE',
              'CRUK', 'PADS', 'D', 'S', 'GIFT']
df = df[~df['stock_code'].astype(str).str.upper().isin(junk_codes)]
```

### 7.5 Handle missing descriptions and trim text

```python
df['description'] = df['description'].astype(str).str.strip().str.upper()
df = df[df['description'].notna() & (df['description'] != 'NAN')]
```

### 7.6 Remove duplicates

```python
before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df):,} exact duplicate rows")
```

### 7.7 Engineer the revenue column (and a few helpers)

```python
df['revenue'] = df['quantity'] * df['price']

# Time features that will help in EDA and Power BI
df['year']       = df['invoice_date'].dt.year
df['month']      = df['invoice_date'].dt.month
df['month_name'] = df['invoice_date'].dt.strftime('%b')
df['year_month'] = df['invoice_date'].dt.to_period('M').astype(str)  # '2010-12'
df['day_of_week']= df['invoice_date'].dt.day_name()
df['date']       = df['invoice_date'].dt.date
```

### 7.8 Treat extreme outliers (carefully)
Don't blindly delete outliers — a genuine bulk B2B order is real revenue. Inspect first, then decide.

```python
# Inspect the largest line items
df.nlargest(10, 'quantity')[['invoice','description','quantity','price','revenue']]
df.nlargest(10, 'revenue')[['invoice','description','quantity','price','revenue']]

# Optional: flag (don't necessarily drop) statistical outliers using the IQR rule
q1, q3 = df['quantity'].quantile([0.25, 0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print("Rows above quantity outlier threshold:", (df['quantity'] > upper).sum())
# Decision: keep them but note their existence, OR cap for charts only. Document your choice.
```

### 7.9 Final validation and export

```python
# Sanity checks — these should all make sense before you trust the data
assert df['quantity'].min() > 0
assert df['price'].min() > 0
assert df['revenue'].min() > 0
print("Final shape:", df.shape)
print("Date range:", df['invoice_date'].min(), "→", df['invoice_date'].max())
print("Unique products:", df['stock_code'].nunique())
print("Total revenue:", f"{df['revenue'].sum():,.2f}")

# Save the clean dataset — this single file feeds SQL and Power BI
df.to_csv('../data/processed/sales_clean.csv', index=False)
```

> **Document your cleaning log** in the notebook and README, e.g.: *"Started with 1,067,371 rows → removed X cancellations, Y invalid prices, Z junk codes, W duplicates → final 805,xxx valid sale lines."* That before/after audit trail is exactly what reviewers and interviewers look for.

---

## 8. Phase 3 — Exploratory Data Analysis (Python + Matplotlib)

Goal: explore the clean data and produce the **four key outputs** as charts. Do this in `notebooks/02_eda.ipynb`. EDA is iterative — chart, observe, ask a follow-up question, chart again.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/processed/sales_clean.csv', parse_dates=['invoice_date'])

plt.rcParams['figure.figsize'] = (12, 5)
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
```

> **Charting habits that make you look professional:** always add a **title**, **axis labels**, and **units**; format large numbers (thousands separators); save each figure with `plt.savefig('../reports/figures/<name>.png', dpi=150, bbox_inches='tight')` so you can reuse them in your report.

### 8.1 KEY OUTPUT 1 — Demand trends (over time)

**Monthly revenue and units sold.** Are we growing?

```python
monthly = (df.groupby('year_month')
             .agg(revenue=('revenue', 'sum'),
                  units=('quantity', 'sum'),
                  orders=('invoice', 'nunique'))
             .reset_index())
monthly['year_month'] = pd.to_datetime(monthly['year_month'])
monthly = monthly.sort_values('year_month')

fig, ax1 = plt.subplots()
ax1.plot(monthly['year_month'], monthly['revenue'], marker='o', color='tab:blue', label='Revenue')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue', color='tab:blue')
ax1.set_title('Monthly Revenue Trend')

ax2 = ax1.twinx()   # second axis for units
ax2.plot(monthly['year_month'], monthly['units'], marker='s', color='tab:orange', alpha=0.6, label='Units')
ax2.set_ylabel('Units Sold', color='tab:orange')
ax2.grid(False)

plt.tight_layout()
plt.savefig('../reports/figures/01_monthly_trend.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Add a moving average** to separate signal from noise:

```python
monthly['rev_ma3'] = monthly['revenue'].rolling(3).mean()  # 3-month moving average

plt.plot(monthly['year_month'], monthly['revenue'], marker='o', alpha=0.4, label='Monthly revenue')
plt.plot(monthly['year_month'], monthly['rev_ma3'], color='red', linewidth=2, label='3-month moving avg')
plt.title('Revenue Trend with 3-Month Moving Average')
plt.xlabel('Month'); plt.ylabel('Revenue'); plt.legend()
plt.show()
```

**Month-over-month growth %** (the number stakeholders care about):

```python
monthly['mom_growth_%'] = monthly['revenue'].pct_change() * 100
monthly[['year_month', 'revenue', 'mom_growth_%']].round(1)
```

> *What to look for:* an overall upward/downward slope (trend), and any single month that jumps far above the moving-average line (a spike — investigate it in 8.3).

### 8.2 KEY OUTPUT 2 — Top & bottom products

Note that **top by units ≠ top by revenue**. A cheap item can sell in huge volume but contribute little money; a pricey item can rank high on revenue with modest volume. Show both.

```python
# Top 10 by REVENUE
top_rev = (df.groupby('description')['revenue'].sum()
             .sort_values(ascending=False).head(10))

plt.barh(top_rev.index[::-1], top_rev.values[::-1], color='tab:green')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.tight_layout()
plt.savefig('../reports/figures/02_top_products_revenue.png', dpi=150, bbox_inches='tight')
plt.show()

# Top 10 by UNITS SOLD
top_units = (df.groupby('description')['quantity'].sum()
               .sort_values(ascending=False).head(10))
plt.barh(top_units.index[::-1], top_units.values[::-1], color='tab:blue')
plt.title('Top 10 Products by Units Sold')
plt.xlabel('Units'); plt.tight_layout(); plt.show()
```

**Bottom products** (slow movers — candidates to discontinue):

```python
# Among products that sold at least once, the weakest performers
prod_units = df.groupby('description')['quantity'].sum().sort_values()
bottom = prod_units.head(10)
print("Slowest-moving products:\n", bottom)
```

> *Tip:* compute the top-by-revenue and top-by-units lists side by side and call out products that appear on one list but not the other. That contrast ("high volume, low value" vs "low volume, high value") is a great insight to highlight.

### 8.3 KEY OUTPUT 3 — Seasonal spikes

**Total revenue by calendar month** (aggregating across years to expose the seasonal shape):

```python
by_month = (df.groupby('month')['revenue'].sum()
              .reindex(range(1, 13)))
month_labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

plt.bar(month_labels, by_month.values, color='tab:purple')
plt.title('Revenue by Calendar Month (Seasonality)')
plt.ylabel('Revenue')
plt.savefig('../reports/figures/03_seasonality_month.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Day-of-week pattern** (useful for staffing / promo timing):

```python
dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
by_dow = (df.groupby('day_of_week')['revenue'].sum().reindex(dow_order))
plt.bar(by_dow.index, by_dow.values, color='tab:cyan')
plt.title('Revenue by Day of Week'); plt.ylabel('Revenue')
plt.xticks(rotation=45); plt.tight_layout(); plt.show()
```

**Month × Year heatmap** (see whether the seasonal pattern repeats each year):

```python
pivot = df.pivot_table(index='month', columns='year',
                       values='revenue', aggfunc='sum')

fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(pivot, aspect='auto', cmap='YlOrRd')
ax.set_xticks(range(len(pivot.columns)), pivot.columns)
ax.set_yticks(range(12), month_labels)
ax.set_title('Revenue Heatmap: Month vs Year')
fig.colorbar(im, ax=ax, label='Revenue')
plt.tight_layout(); plt.show()
# (If you installed seaborn: sns.heatmap(pivot, annot=True, fmt=',.0f', cmap='YlOrRd') is prettier.)
```

**(Optional, advanced) Seasonal decomposition** — formally split the series into trend + seasonal + residual:

```python
from statsmodels.tsa.seasonal import seasonal_decompose

ts = (df.set_index('invoice_date')['revenue']
        .resample('W').sum())          # weekly totals
result = seasonal_decompose(ts, model='additive', period=52)
result.plot()
plt.tight_layout(); plt.show()
```

> *What to look for:* one or two months standing well above the rest (e.g., a pre-holiday Q4 surge). Confirm in the heatmap that it recurs across years rather than being a one-off.

### 8.4 KEY OUTPUT 4 — Revenue contribution analysis (Pareto / 80-20)

The classic finding: a small share of products drives most of the revenue. Quantify it.

```python
prod_rev = df.groupby('description')['revenue'].sum().sort_values(ascending=False)

cum_pct = prod_rev.cumsum() / prod_rev.sum() * 100
n_products = len(prod_rev)

# How many products make up 80% of revenue?
n_for_80 = int((cum_pct <= 80).sum()) + 1
print(f"{n_for_80} of {n_products} products "
      f"({n_for_80/n_products*100:.1f}%) generate 80% of revenue")

# Pareto chart: bars = revenue per product, line = cumulative %
top_n = prod_rev.head(30)
top_cum = top_n.cumsum() / prod_rev.sum() * 100

fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.bar(range(len(top_n)), top_n.values, color='tab:blue')
ax1.set_ylabel('Revenue', color='tab:blue')
ax1.set_xticks(range(len(top_n)))
ax1.set_xticklabels(top_n.index, rotation=90, fontsize=7)

ax2 = ax1.twinx()
ax2.plot(range(len(top_n)), top_cum.values, color='red', marker='o')
ax2.axhline(80, color='grey', linestyle='--')
ax2.set_ylabel('Cumulative % of revenue', color='red')
ax2.set_ylim(0, 105); ax2.grid(False)

plt.title('Pareto Analysis — Revenue Contribution by Product (Top 30)')
plt.tight_layout()
plt.savefig('../reports/figures/04_pareto.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Revenue by country/region** (if your dataset has geography):

```python
by_geo = (df.groupby('country')['revenue'].sum()
            .sort_values(ascending=False).head(10))
plt.barh(by_geo.index[::-1], by_geo.values[::-1], color='tab:olive')
plt.title('Top 10 Markets by Revenue'); plt.xlabel('Revenue')
plt.tight_layout(); plt.show()
```

> *What to look for:* the headline Pareto number ("the top X% of products = 80% of revenue") and any heavy concentration in one market — both have direct inventory/marketing implications you'll write up in Phase 6.

### 8.5 Wrap up the EDA
For each chart, write 1–2 sentences of observation directly in the notebook (markdown cells). Those observations become the raw material for your insights section. EDA isn't done when the charts exist — it's done when you can *say what each one means*.

---

## 9. Phase 4 — SQL Analysis

Goal: reproduce and extend the analysis using SQL. This proves you can answer business questions directly against a database — a core analyst skill. The queries below are written for **PostgreSQL**; **SQLite** differences are flagged with `⚠️ SQLite`.

### 9.1 Load the clean data into a database

**Option A — SQLite (fastest, from Python):**

```python
import sqlite3, pandas as pd
df = pd.read_csv('../data/processed/sales_clean.csv', parse_dates=['invoice_date'])
conn = sqlite3.connect('../data/processed/sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()
# Now open sales.db in DB Browser for SQLite and run queries.
```

**Option B — PostgreSQL (from Python via SQLAlchemy):**

```python
from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv('../data/processed/sales_clean.csv', parse_dates=['invoice_date'])
engine = create_engine('postgresql+psycopg2://USER:PASSWORD@localhost:5432/sales_db')
df.to_sql('sales', engine, if_exists='replace', index=False)
```

If you prefer to create the table by hand first, here is `sql/00_create_table.sql`:

```sql
CREATE TABLE sales (
    invoice       VARCHAR(20),
    stock_code    VARCHAR(20),
    description   VARCHAR(255),
    quantity      INTEGER,
    price         NUMERIC(10,2),
    revenue       NUMERIC(12,2),
    invoice_date  TIMESTAMP,
    country       VARCHAR(100),
    customer_id   VARCHAR(20)
);
-- then COPY (Postgres) or .import (SQLite) the CSV into it.
```

### 9.2 Sanity check (always validate after loading)

```sql
SELECT COUNT(*)                       AS row_count,
       MIN(invoice_date)              AS first_sale,
       MAX(invoice_date)              AS last_sale,
       COUNT(DISTINCT stock_code)     AS num_products,
       ROUND(SUM(revenue), 2)         AS total_revenue
FROM sales;
```

The `total_revenue` here should match the number you printed at the end of Python cleaning. If it doesn't, something went wrong in the load.

### 9.3 KEY OUTPUT 1 — Demand trends (monthly)

```sql
SELECT
    DATE_TRUNC('month', invoice_date) AS month,
    SUM(revenue)                      AS revenue,
    SUM(quantity)                     AS units,
    COUNT(DISTINCT invoice)           AS orders
FROM sales
GROUP BY DATE_TRUNC('month', invoice_date)
ORDER BY month;
-- ⚠️ SQLite: replace DATE_TRUNC('month', invoice_date)
--    with strftime('%Y-%m', invoice_date)
```

**Month-over-month growth using a window function (`LAG`):**

```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', invoice_date) AS month,
           SUM(revenue) AS revenue
    FROM sales
    GROUP BY 1
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND( 100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
                  / LAG(revenue) OVER (ORDER BY month), 1) AS mom_growth_pct
FROM monthly
ORDER BY month;
```

### 9.4 KEY OUTPUT 2 — Top & bottom products

```sql
-- Top 10 products by revenue
SELECT description,
       SUM(quantity) AS units,
       ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY description
ORDER BY revenue DESC
LIMIT 10;

-- Top 10 by units sold
SELECT description, SUM(quantity) AS units
FROM sales
GROUP BY description
ORDER BY units DESC
LIMIT 10;

-- Bottom 10 (slowest movers)
SELECT description, SUM(quantity) AS units
FROM sales
GROUP BY description
ORDER BY units ASC
LIMIT 10;
```

**Rank products and bucket them** with `RANK()`:

```sql
SELECT description,
       ROUND(SUM(revenue), 2) AS revenue,
       RANK() OVER (ORDER BY SUM(revenue) DESC) AS revenue_rank
FROM sales
GROUP BY description
ORDER BY revenue_rank
LIMIT 20;
```

### 9.5 KEY OUTPUT 3 — Seasonal spikes

```sql
-- Revenue by calendar month (seasonality), averaged across years
SELECT
    EXTRACT(MONTH FROM invoice_date) AS month_num,
    ROUND(SUM(revenue), 2)           AS total_revenue,
    ROUND(AVG(revenue), 2)           AS avg_line_revenue
FROM sales
GROUP BY 1
ORDER BY 1;
-- ⚠️ SQLite: EXTRACT(MONTH FROM invoice_date)
--    becomes CAST(strftime('%m', invoice_date) AS INTEGER)

-- Revenue by day of week
SELECT
    TO_CHAR(invoice_date, 'Day') AS weekday,
    ROUND(SUM(revenue), 2)       AS revenue
FROM sales
GROUP BY 1, EXTRACT(DOW FROM invoice_date)
ORDER BY EXTRACT(DOW FROM invoice_date);
```

**Identify spike months** — months whose revenue is well above the overall monthly average:

```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', invoice_date) AS month,
           SUM(revenue) AS revenue
    FROM sales GROUP BY 1
)
SELECT month, revenue,
       ROUND(AVG(revenue) OVER (), 2)                       AS avg_month_revenue,
       ROUND(100.0 * revenue / AVG(revenue) OVER () - 100, 1) AS pct_above_avg
FROM monthly
ORDER BY pct_above_avg DESC;
```

### 9.6 KEY OUTPUT 4 — Revenue contribution (Pareto in SQL)

```sql
WITH product_rev AS (
    SELECT description, SUM(revenue) AS revenue
    FROM sales
    GROUP BY description
),
ranked AS (
    SELECT description,
           revenue,
           SUM(revenue) OVER (ORDER BY revenue DESC
                              ROWS UNBOUNDED PRECEDING) AS running_revenue,
           SUM(revenue) OVER ()                         AS total_revenue,
           ROW_NUMBER() OVER (ORDER BY revenue DESC)    AS product_rank
    FROM product_rev
)
SELECT description,
       ROUND(revenue, 2)                                       AS revenue,
       product_rank,
       ROUND(100.0 * running_revenue / total_revenue, 2)       AS cumulative_pct
FROM ranked
ORDER BY product_rank;
```

Read the result top-down: the row where `cumulative_pct` first crosses 80 tells you **how many products account for 80% of revenue** — your Pareto headline, now reproduced in SQL.

**Revenue share by market:**

```sql
SELECT country,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(100.0 * SUM(revenue) / SUM(SUM(revenue)) OVER (), 2) AS pct_of_total
FROM sales
GROUP BY country
ORDER BY revenue DESC;
```

### 9.7 Save your queries
Put all of these in `sql/01_analysis_queries.sql` with a comment header above each block describing the question it answers. This file alone demonstrates solid SQL competency to anyone reviewing the project.

> **Why do SQL *and* Pandas if they overlap?** Two reasons. (1) It validates your work — the numbers from both should agree. (2) It shows range: many roles expect SQL specifically. Treat the agreement between Pandas and SQL totals as a built-in correctness check.

---

## 10. Phase 5 — Power BI Dashboard

Goal: build an interactive, multi-page dashboard that lets a stakeholder explore the four key outputs themselves. This is where the project becomes a *product*. Follow the steps in order.

### 10.1 Get data in

1. Open **Power BI Desktop** → **Home → Get Data → Text/CSV** → select `data/processed/sales_clean.csv`.
   - *(Connecting to PostgreSQL instead? Use **Get Data → PostgreSQL database**, enter `localhost` / `sales_db`, pick the `sales` table.)*
2. In the preview, click **Transform Data** to open **Power Query** before loading. Always inspect here first.
3. In Power Query, verify column **data types** (the icon on each header): `invoice_date` = Date/Time, `quantity` = Whole Number, `price`/`revenue` = Decimal Number, text columns = Text. Fix any that imported wrong.
4. Even though you cleaned in Python, do a final check here: **remove blank rows**, confirm no error values. Then **Home → Close & Apply**.

> Keeping Python as the heavy-cleaning layer and Power Query as a light final-check layer is a clean, defensible architecture you can explain in an interview.

### 10.2 Build a Date table (essential for time intelligence)

Power BI's month-over-month / year-over-year functions need a proper, continuous **date dimension**. Create one with DAX: **Modeling → New Table**:

```DAX
Date =
ADDCOLUMNS(
    CALENDAR(MIN(sales[invoice_date]), MAX(sales[invoice_date])),
    "Year",        YEAR([Date]),
    "Month Number",MONTH([Date]),
    "Month",       FORMAT([Date], "MMM"),
    "Month-Year",  FORMAT([Date], "MMM YYYY"),
    "Quarter",     "Q" & FORMAT([Date], "Q"),
    "Day of Week", FORMAT([Date], "ddd"),
    "Weekday Num", WEEKDAY([Date], 2)
)
```

Then:
1. **Sort the Month column correctly:** select the `Month` column → **Column tools → Sort by Column → Month Number** (otherwise months sort alphabetically: Apr, Aug, Dec…).
2. Do the same for `Day of Week` → sort by `Weekday Num`.
3. **Mark as date table:** select the Date table → **Table tools → Mark as Date Table** → choose `[Date]`.

### 10.3 Create the relationship (data model)

Go to **Model view**. Drag **`Date[Date]`** onto **`sales[invoice_date]`** to create a one-to-many relationship (one date → many sales). You now have a simple **star schema**: a `sales` fact table linked to a `Date` dimension. (If using Superstore, you can likewise build separate Product/Category and Region dimensions for a fuller star schema, but a single fact + Date table is perfectly fine for this project.)

### 10.4 Write the core DAX measures

Create a dedicated measures area: **New Measure** (right-click the `sales` table → New measure). Add these one at a time.

```DAX
Total Revenue = SUM(sales[revenue])
```
```DAX
Total Units = SUM(sales[quantity])
```
```DAX
Total Orders = DISTINCTCOUNT(sales[invoice])
```
```DAX
Average Order Value = DIVIDE([Total Revenue], [Total Orders])
```
```DAX
Revenue MoM % =
VAR Curr = [Total Revenue]
VAR Prev = CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, MONTH))
RETURN DIVIDE(Curr - Prev, Prev)
```
```DAX
Revenue YoY % =
VAR Curr = [Total Revenue]
VAR Prev = CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, YEAR))
RETURN DIVIDE(Curr - Prev, Prev)
```
```DAX
Running Total Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(ALLSELECTED('Date'[Date]), 'Date'[Date] <= MAX('Date'[Date]))
)
```
```DAX
% of Total Revenue =
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(sales[description]))
)
```

Set formatting for each measure (**Measure tools → Format**): currency for revenue/AOV, whole number for units/orders, percentage for the % measures.

### 10.5 Build the report pages

A clean four-page structure maps directly onto your four key outputs.

**PAGE 1 — Executive Overview**
- Four **KPI Cards** at the top: `Total Revenue`, `Total Units`, `Total Orders`, `Average Order Value`.
- A **Line chart**: Axis = `Date[Month-Year]`, Values = `Total Revenue` → the headline **demand trend**.
- A **Clustered bar chart**: revenue by `country` (or `category`) → top markets.
- A **Card** or **KPI visual** showing `Revenue MoM %` (use conditional formatting: green up / red down).
- A **Map** (if you have geography): Location = `country`, Size = `Total Revenue`.

**PAGE 2 — Product Analysis (Top & Bottom)**
- **Bar chart — Top 10 by revenue:** Axis = `description`, Values = `Total Revenue`; then use the visual's **filter → Top N → Top 10 by Total Revenue**.
- **Bar chart — Top 10 by units:** same idea with `Total Units`.
- **Bar chart — Bottom 10:** Top N → **Bottom 10** by `Total Units`.
- **Table** with `description`, `Total Units`, `Total Revenue`, `% of Total Revenue`; apply **conditional formatting** (data bars on revenue) to make leaders pop.

**PAGE 3 — Seasonality & Trends**
- **Column chart:** Axis = `Date[Month]` (sorted by Month Number), Values = `Total Revenue` → the **seasonal shape**.
- **Matrix (heatmap):** Rows = `Date[Month]`, Columns = `Date[Year]`, Values = `Total Revenue`; turn on **conditional formatting → background color** so high months glow — a Power BI heatmap.
- **Line chart with `Running Total Revenue`** to show cumulative build-up through the year.
- **Column chart:** revenue by `Date[Day of Week]` (sorted) for weekly patterns.

**PAGE 4 — Revenue Contribution (Pareto)**
- **Pareto:** a combo chart (**Line and clustered column**) — Column = `Total Revenue` by `description`, Line = a cumulative-% measure. The simplest route is to add the built-in or a custom **Pareto/ABC** visual; alternatively create a cumulative measure and plot it as the line.
- **Donut/Treemap:** revenue by `category` or top products → contribution share at a glance.
- A **text/card callout** stating the Pareto headline (e.g., "Top N products = 80% of revenue").

### 10.6 Make it interactive

- **Slicers:** add slicers for `Date[Year]`, `Date[Month]`, and `country`/`category` so users filter the whole page. Consider a **date-range slider** slicer.
- **Sync slicers** across pages: **View → Sync slicers** so a filter set on one page carries to others.
- **Drill-through:** create a hidden detail page and right-click → **Drill-through** on a product to inspect it.
- **Tooltips:** customize hover tooltips to show extra measures.
- **Cross-filtering:** clicking a bar on one visual filters the others — this is on by default; test it.

### 10.7 Polish (this is what separates good from average)

- Apply a consistent **theme**: **View → Themes** (pick one and stick to it). Keep a limited, professional color palette.
- Give every visual a clear **title** and remove chart junk you don't need.
- Align and size visuals on a grid; group related visuals.
- Add a **title bar** with the report name and a short subtitle.
- Format numbers sensibly (thousands separators, no excessive decimals).
- Add a small **"Last refreshed"** text and a one-line data-source note.

### 10.8 Save & share
Save as `powerbi/sales_dashboard.pbix`. To share without Power BI Service, **File → Export → PDF**, and take clean **screenshots** of each page for your README and portfolio. (If you have a free Power BI account, **Publish** to the Service to get a shareable web link.)

---

## 11. Phase 6 — Business Insights

Goal: convert the charts and query results into **insights** and **recommendations**. This is the part that turns a technical exercise into business value — and it's what interviewers probe hardest. A chart is not an insight; an insight says *what it means* and *what to do about it*.

### 11.1 The insight formula
For each finding, write it in this structure:

> **Observation** (what the data shows) → **Interpretation** (why it matters) → **Recommendation** (what to do) → **Expected impact / metric to watch.**

### 11.2 Worked examples for each key output

*(These are illustrative templates. Replace the bracketed values with your actual numbers.)*

**Demand trends**
> *Observation:* Monthly revenue grew from `£X` to `£Y` over the period, a `[+Z%]` increase, with the steepest growth in `[quarter]`.
> *Interpretation:* Underlying demand is expanding, not just one-off spikes — the moving average trends upward.
> *Recommendation:* Scale inventory and fulfillment capacity to match the trajectory; revisit demand forecasts upward.
> *Watch:* Month-over-month growth %, to catch any slowdown early.

**Top & bottom products**
> *Observation:* The top `[N]` products by revenue are `[list]`; several top-by-volume items (`[list]`) are low-priced and contribute little revenue.
> *Interpretation:* A few SKUs are the commercial engine, while many high-volume items are low-margin traffic drivers. The bottom `[N]` products sold in negligible quantities.
> *Recommendation:* Protect availability of the revenue leaders (never stock out); review the slow movers for **discontinuation** or clearance to free up working capital and shelf/warehouse space.
> *Watch:* Stockout rate on top SKUs; inventory turnover on the long tail.

**Seasonal spikes**
> *Observation:* Revenue peaks sharply in `[month(s)]`, running `[+%]` above the monthly average, and the pattern **recurs across years** in the heatmap.
> *Interpretation:* This is genuine seasonality (e.g., pre-holiday demand), not noise — it's predictable and plannable.
> *Recommendation:* Build inventory and staffing ahead of the peak; concentrate marketing spend in the **run-up** weeks; secure supplier capacity early.
> *Watch:* Sell-through during the peak window; pre-season stock cover.

**Revenue contribution (Pareto)**
> *Observation:* The top `[X%]` of products generate `~80%` of revenue; the top `[market]` accounts for `[%]` of sales.
> *Interpretation:* Revenue is highly concentrated — both in product range and (possibly) geography. That's an efficiency opportunity and a risk.
> *Recommendation:* Focus merchandising, promotions, and inventory investment on the vital few; rationalize the long tail. Mitigate concentration risk by testing growth in secondary markets/products.
> *Watch:* Share of revenue from top-20% SKUs over time; revenue diversification across markets.

### 11.3 Make the insights credible
- **Quantify everything** — "+18%", "top 14 of 3,800 products", "£X". Vague insights ("sales are good") carry no weight.
- **Cross-check** Pandas vs SQL numbers; if they disagree, resolve it before reporting.
- **Acknowledge limitations** — e.g., "data covers a single retailer over ~2 years; cancellations were excluded; no cost data, so this is revenue not profit." Honesty about scope is a strength, not a weakness.
- **Tie back to decisions** — every recommendation should map to an action someone could actually take (buy more of X, drop Y, schedule a Q4 campaign).

### 11.4 Capture it
Write these up in `reports/insights.md`, embedding the exported figures. Aim for ~5–8 crisp insights, not 30 shallow ones.

---

## 12. Phase 7 — Conclusions, Documentation & Portfolio Write-up

Goal: package the project so a stranger (recruiter, hiring manager, teammate) understands it in two minutes.

### 12.1 Write the conclusion
Summarize, in a few sentences: the business question, what you found (the headline numbers), and the top 2–3 recommendations. Then a short **"what I'd do next"** (the stretch goals in Appendix D) — this signals you understand the project's limits and how to extend it.

### 12.2 Write a strong README
Structure for `README.md`:

```
# Sales & Demand Analysis

## Overview
One paragraph: the business problem and what this project delivers.

## Tools & Skills
Python (Pandas, Matplotlib) · SQL · Power BI

## Data
Source, size, date range, grain, and a link/note. State that raw data isn't committed if it's large/licensed.

## Process
1. Cleaning (Python)  2. EDA (Matplotlib)  3. SQL analysis  4. Power BI dashboard

## Key Findings   ← put 4–6 bullet insights with NUMBERS here
- Revenue grew +X% ...
- Top X% of products drive 80% of revenue ...
- December demand runs +Y% above average ...

## Dashboard
[embed 2–3 screenshots of the Power BI pages]

## Repository Structure
[the folder tree]

## How to Reproduce
Setup steps: install requirements, run notebooks in order, load DB, open .pbix.
```

> The **Key Findings** section is the most-read part. Lead with numbers and outcomes, not methods.

### 12.3 Put it on GitHub
- Add a `.gitignore` (ignore large raw data, `venv/`, checkpoints).
- Commit notebooks **with outputs visible** so the work renders on GitHub without running anything.
- Include the dashboard **screenshots/PDF** (and the `.pbix` if size allows).
- Use a clear repo name and a one-line description.

### 12.4 Prepare to talk about it
Be ready to answer: *Why did you remove those rows? Why both SQL and Pandas? What surprised you? What would you do with more time/data? What decision would your top recommendation change?* Having crisp answers turns the project into a strong interview asset.

---

## Appendix A — Project Checklist

```
Setup
[ ] Folder structure created
[ ] Environment + libraries installed
[ ] Database engine installed
[ ] Power BI Desktop installed

Data
[ ] Dataset downloaded into data/raw/
[ ] Data dictionary written
[ ] First-look diagnostics run (shape, dtypes, nulls, duplicates)

Cleaning (Python)
[ ] Column names standardized
[ ] Dates parsed
[ ] Cancellations / returns removed
[ ] Junk codes removed
[ ] Duplicates removed
[ ] revenue + time features engineered
[ ] Outliers inspected and decision documented
[ ] Validation asserts pass
[ ] sales_clean.csv exported
[ ] Cleaning log written (before → after counts)

EDA (Matplotlib)
[ ] Demand trend (monthly + moving average + MoM%)
[ ] Top products (revenue AND units) + bottom products
[ ] Seasonality (by month, day of week, heatmap)
[ ] Pareto / revenue contribution
[ ] Every chart titled, labelled, saved
[ ] Observations written per chart

SQL
[ ] Clean data loaded into DB
[ ] Load validated against Python totals
[ ] Queries for all 4 outputs written
[ ] Window-function queries (LAG, RANK, running total) included
[ ] Queries saved to .sql with comments

Power BI
[ ] Data imported + types checked
[ ] Date table created, sorted, marked
[ ] Relationship built
[ ] Core measures written + formatted
[ ] 4 report pages built
[ ] Slicers + interactions working
[ ] Theme + formatting polished
[ ] Saved + exported (screenshots/PDF)

Insights & Delivery
[ ] insights.md with 5–8 quantified insights
[ ] Limitations stated
[ ] README written with Key Findings
[ ] Pushed to GitHub
```

---

## Appendix B — Suggested Timeline

A realistic part-time pace (adjust to your schedule):

| Stage | Effort |
|-------|--------|
| Setup + data understanding | ~half a day |
| Cleaning (Python) | ~1 day |
| EDA + charts | ~1–2 days |
| SQL analysis | ~1 day |
| Power BI dashboard | ~1–2 days |
| Insights + README + polish | ~1 day |

Build in this order — don't jump to Power BI before cleaning. Each phase depends on the previous one's output.

---

## Appendix C — Common Pitfalls

- **Cleaning inside Power BI instead of upstream.** Do heavy cleaning once in Python so SQL and Power BI agree. Power Query is for final touch-ups only.
- **Forgetting the Date table in Power BI.** Time-intelligence DAX (MoM/YoY) silently misbehaves without a proper, continuous, marked date dimension.
- **Months sorting alphabetically.** Always "Sort by Column" → Month Number.
- **Confusing revenue rank with volume rank.** Report both; the contrast is an insight.
- **Deleting outliers blindly.** A huge order may be a real B2B sale. Inspect, then decide, then document.
- **Wrong file encoding.** Online Retail needs `encoding='ISO-8859-1'`.
- **Counting cancellations as sales.** Remove `C` invoices and non-positive quantities, or every total is inflated.
- **Pandas and SQL totals disagree.** Usually a cleaning step applied in one place but not the other — reconcile before trusting either.
- **Charts without titles/labels/units.** Unlabelled charts read as unfinished work.
- **Insights with no numbers.** "Sales are seasonal" is weak; "December revenue is +X% above the monthly average, recurring across both years" is strong.

---

## Appendix D — Stretch Goals (to stand out)

- **RFM / customer segmentation** (Recency, Frequency, Monetary) if customer IDs are present.
- **Cohort / retention analysis** by first-purchase month.
- **Simple demand forecasting** (e.g., statsmodels Holt-Winters / SARIMA, or Prophet) projecting next-quarter demand.
- **ABC inventory classification** building on the Pareto analysis.
- **Profit analysis** instead of just revenue (Superstore has a `Profit` column).
- **Basket analysis** (which products are bought together) using association rules.
- **Automate the pipeline** so raw → clean → DB runs from a single script.

---

## Appendix E — Resources

- **Pandas:** official docs → *User Guide* and *10 minutes to pandas*.
- **Matplotlib:** official *Pyplot tutorial* and the *gallery* for chart recipes.
- **SQL window functions:** PostgreSQL docs → *Window Functions Tutorial*; practice on Mode SQL Tutorial or StrataScratch.
- **Power BI:** Microsoft Learn → *Power BI* learning paths; *DAX Guide* (dax.guide) for measure syntax.
- **Datasets:** Kaggle (search "Online Retail II", "Sample Superstore"); UCI Machine Learning Repository.

---

### Final word
Build it in order, validate as you go (Pandas vs SQL), and spend real effort on the **insights** and **README** — that's where most people under-invest and where you can clearly stand out. Good luck; you have everything here to build it independently.
