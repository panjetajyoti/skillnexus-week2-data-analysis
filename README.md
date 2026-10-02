# SkillNexus Data Analyst Course - Week 2 Assignments

Complete implementation and solutions for Week 2 coursework covering Python data manipulation and SQL query engineering.

---

## 📁 Repository Structure

```text
├── python_analysis.py    # Python scripts solving all 5 practice set questions
├── sql_queries.sql       # SQL queries for aggregations, joins, and customer segmentation
└── README.md             # Project documentation and summary
```
# 🐍 Part 1: Python for Data Analysis
## File: python_analysis.py
| Sr. No. | Task | Implementation / Method |
| :---: | :--- | :--- |
| 1 | **Load CSV & Basic Info** | Read dataset with `pd.read_csv()`, inspected metadata with `.info()` and `.describe()`. |
| 2 | **Handle Missing Values & Duplicates** | De-duplicated using `.drop_duplicates()`; imputed numeric null values with the median. |
| 3 | **Category Grouping & Revenue** | Aggregated total revenue by product category via `.groupby('Category')['Revenue'].sum()`. |
| 4 | **Multi-Column Sorting** | Sorted via `.sort_values(by=['Category', 'Revenue'], ascending=[True, False])`. |
| 5 | **Correlation Matrix** | Generated numerical feature correlation matrix using `.corr()`. |
# 🗄️ Part 2: SQL for Data Analysis
## File: sql_queries.sql

* Top Customers by Total Spend: Uses INNER JOIN, GROUP BY, SUM(), and ORDER BY to rank top customers by total order spend.
* Average Order Value (AOV): Calculates average order value per customer filtered using HAVING COUNT(o.order_id) > 1.
* Customer Segmentation: Uses a subquery and CASE conditional statement to segment users into VIP, Mid-Tier, and Standard   tiers based on lifetime spend.
# 🚀 Execution
## Run the Python pipeline locally:
```
python python_analysis.py
```
