import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="proba")
cursor=conn.cursor()
selectquery= "select * from proba"


cursor.execute(selectquery)
records = cursor.fetchall()
print("row count", cursor.rowcount)

for row in records:
    print(row[0])
	
cursor.close()
conn.close()