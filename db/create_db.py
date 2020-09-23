import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="iot",
    passwd="DataProcess-10",
    database='iot'
)

try:
    mycursor = db.cursor()
except:  # catch *all* exceptions
    e = sys.exc_info()
    print(e)

try:
    mycursor.execute("CREATE DATABASE iot")
except:  # catch *all* exceptions
    e = sys.exc_info()
    print(e)

try:
    mycursor.execute("CREATE TABLE sensor (id int PRIMARY KEY auto_increment ,name VARCHAR(50), type VARCHAR(50))")

except:  # catch *all* exceptions
    e = sys.exc_info()
    print(e)

try:
    mycursor.execute("DESCRIBE sensor")
    for x in mycursor:
        print(x)
    mycursor.execute("INSERT INTO SENSOR (NAME,TYPE) VALUES(%s,%s)", ("sensor 1", "temperature"))
    mycursor.execute("INSERT INTO SENSOR (NAME,TYPE) VALUES(%s,%s)", ("sensor 2", "temperature"))
    mycursor.execute("INSERT INTO SENSOR (NAME,TYPE) VALUES(%s,%s)", ("sensor 3", "TDS"))
    db.commit()
except:  # catch *all* exceptions:q!

    e = sys.exc_info()
    print(e)
