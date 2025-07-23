CHINOOK MUSIC STORE Data Analysis (SQL + Visualisations)

This project explores the Chinook music store database using SQL in PostgreSQL. It answers a variety of business and music-related questions, offering insights into sales performance, customer behavior, artist popularity, and inventory details. In addition to raw SQL analysis, the project includes key visualisations to communicate findings effectively.

## 📁 Project Structure

- `chinook_database` - Raw database file and schema(PNG)
- `sql_queries` – Contains SQL scripts used to analyze the database
- `visualisations` – Charts created from analysis results (PNG)
- `scripts` - Python script to run some queries and plots
- `Notebook` -  Jupyter notebook with pandas + matplotlib visualisations
- `README.md` – Overview of the project (this file)

---
What I analysed:
🎵 MUSIC & MEDIA:

1. Top 10 popular tracks by sales
2. Genres with the most tracks
3. Albums with the most tracks
4. Most common media types
5. Playlists with the most tracks

💰 SALES & REVENUE:

6. Countries with the highest revenue
7. Top 5 customers by spending
8. Average invoice total by country
9. Sales by month or year
10. Revenue per genre

👥 CUSTOMERS & EMPLOYEES:

11. Employees supporting the most customers
12. Customers with the most purchases
13. Customer count per country
14. Employees generating the most sales

🎨 ARTISTS & ALBUMS:

15. Artists with the most albums
16. Artists whose tracks make the most revenue
17. Average tracks per album per artist

📦 INVENTORY:

18. Number of tracks per media type
19. Longest track duration
20. Average track length per genre

## 📈 Visualisations

To support the SQL analysis, I've created the following data visualizations:

21. Monthly revenue trends
22. Revenue by physical vs digital formats
23. Regional revenue analysis
24. Artists without albums or tracks

Visualizations are stored in the `visualisations/` folder. These help translate query results into actionable business insights.

## 📥 Getting Started

1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/chinook-analysis.git
---
2. Load the Chinook database into PostgreSQL (you can find the .sql version online)
3. Use pgAdmin or any SQL tool to run scripts from sql_queries/
4. View visualizations in the visualizations/ folder


TOOLS USED:
- PostgreSQL
- SQL
- pandas, matplotlib, seaborn  libraries
