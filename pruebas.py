import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2pacshaq122",
  database = "basecarros"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuarios")

myresult = mycursor.fetchall()
a = list(myresult[0])
print(a)
print(a[0])