import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# --- DATABASE CONNECTION ---
# Replace these with your actual database credentials
engine = create_engine('postgresql://username:password@localhost:5432/chinook')

# --- Create output folder if it doesn't exist ---
os.makedirs('visualizations', exist_ok=True)

# 1️⃣ Top 10 Tracks by Sales
query = """
SELECT t."Name" AS track_name, SUM(il."Quantity") AS total_sales
FROM "Track" t
JOIN "InvoiceLine" il ON t."TrackId" = il."TrackId"
GROUP BY t."Name"
ORDER BY total_sales DESC
LIMIT 10;
"""
df = pd.read_sql_query(query, engine)
plt.figure(figsize=(8,5))
sns.barplot(x='total_sales', y='track_name', data=df, palette='Blues_d')
plt.title('Top 10 Tracks by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Track Name')
plt.tight_layout()
plt.savefig('visualizations/top_10_tracks.png')
plt.close()

# 2️⃣ Monthly Revenue Over Time
query = """
SELECT 
  DATE_TRUNC('month', i."InvoiceDate") AS month,
  ROUND(SUM(i."Total"), 2) AS monthly_revenue
FROM "Invoice" i
GROUP BY month
ORDER BY month;
"""
df = pd.read_sql_query(query, engine)
plt.figure(figsize=(10,5))
plt.plot(df['month'], df['monthly_revenue'], marker='o')
plt.title('Monthly Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('visualizations/monthly_revenue.png')
plt.close()

# 3️⃣ Regional Revenue
query = """
SELECT 
  CASE 
    WHEN c."Country" IN ('USA', 'Canada', 'Mexico') THEN 'North America'
    WHEN c."Country" IN ('France', 'Germany', 'United Kingdom', 'Italy', 'Spain') THEN 'Europe'
    WHEN c."Country" IN ('Brazil', 'Argentina') THEN 'South America'
    WHEN c."Country" IN ('Australia', 'New Zealand') THEN 'Oceania'
    WHEN c."Country" IN ('India', 'Japan') THEN 'Asia'
    ELSE 'Other'
  END AS region,
  ROUND(SUM(i."Total"), 2) AS regional_revenue
FROM "Customer" c
JOIN "Invoice" i ON c."CustomerId" = i."CustomerId"
GROUP BY region
ORDER BY regional_revenue DESC;
"""
df = pd.read_sql_query(query, engine)
plt.figure(figsize=(8,5))
plt.bar(df['region'], df['regional_revenue'], color='skyblue')
plt.title('Regional Revenue')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/regional_revenue.png')
plt.close()

# 4️⃣ Revenue: Digital vs Physical
query = """
SELECT
  CASE
    WHEN m."Name" IN ('MPEG audio file', 'AAC audio file', 'Protected MPEG-4 video file') THEN 'Digital'
    ELSE 'Physical'
  END AS format_type,
  ROUND(SUM(il."UnitPrice" * il."Quantity"), 2) AS total_revenue
FROM "InvoiceLine" il
JOIN "Track" t ON il."TrackId" = t."TrackId"
JOIN "MediaType" m ON t."MediaTypeId" = m."MediaTypeId"
GROUP BY format_type
ORDER BY total_revenue DESC;
"""
df = pd.read_sql_query(query, engine)
plt.figure(figsize=(7,5))
plt.bar(df['format_type'], df['total_revenue'], color=['#1f77b4', '#ff7f0e'])
plt.title('Revenue: Digital vs Physical Formats')
plt.xlabel('Format Type')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig('visualizations/digital_vs_physical.png')
plt.close()

print("✅ All visualizations saved in 'visualizations/' folder.")
