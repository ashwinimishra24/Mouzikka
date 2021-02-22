import cx_Oracle
import traceback
conn = None
try:
    conn = cx_Oracle.connect("mouzikka/Ashwini24@127.0.0.1/xe")
    print("connected successfully to db")
    print("database version:", conn.version)
    print("db user:", conn.username)
except cx_Oracle.DatabaseError:
    print("db error")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("disconnected")