import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1')

cursor = conn.cursor()

cursor.execute('CREATE DATABASE test_mysql_databse')

cursor.close()
conn.close()
