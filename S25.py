import mysql.connector as mc
from tabulate import tabulate

conn = mc.connect(host='localhost', user='root', password='huzaifa', database='menagerie')
cursor = conn.cursor()
select_query = """
SELECT name, birth, MONTH(birth)
FROM pet
"""
cursor.execute(select_query)
rows = cursor.fetchall()

table_data = [list(row) for row in rows]

table_headers = ["Name", "Birth", "Birth Month"]

print(tabulate(table_data, headers=table_headers))

cursor.close()
conn.close()