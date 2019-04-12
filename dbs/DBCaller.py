import mysql.connector
def getConnected():
    con=mysql.connector.connect(
        host='localhost',database='mydb',
        user='root', password='root')
    return con
