import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Task 1: Plotting with Pandas

#Load a DataFrame called employee_results using SQL
conn = sqlite3.connect('db/lesson.db')

#Join the employees table with the orders table with the line_items table with the products table
#Group by employee_id, and you SELECT the last_name and revenue, where revenue is the sum of price * quantity
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""
#Run the SQL query and load the results into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

#Close the connection
conn.close()

#Plot functionality to create a bar chart where the x axis is the employee last name and the y axis is the revenue
df.plot(x="last_name", y="revenue", kind="bar", color="teal", title="Total Revenue by Employee")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()