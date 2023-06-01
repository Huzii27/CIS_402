import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='huzaifa')
cursor = conn.cursor()
cursor.close()
conn.close()