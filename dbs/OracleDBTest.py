import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    cursor.execute("select sysdate from dual")
    row =cursor.fetchone()
    for e in row:
        print(e)
    cursor.close()
    db.close()
except Exception as e:
    print(e) 
finally:
    print("Closing database")   
    #db.close()
