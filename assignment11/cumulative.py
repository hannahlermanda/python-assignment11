#Task 2: A Line Plot with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Load DataFrame
conn = sqlite3.connect('db/lesson.db')

#Create a DataFrame with the order_id and the total_price for each order
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

#Run the SQL query and load the results into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

#Close the connection
conn.close()

#Add a "cumulative" column to the DataFrame
df['cumulative'] = df['total_price'].cumsum()

#Use Pandas plotting to create a line plot of cumulative revenue vs order_id
df.plot(x='order_id', y='cumulative', kind='line', title='Cumulative Revenue by Order')
plt.tight_layout()
plt.show()

