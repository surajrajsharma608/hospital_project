import sqlite3

def create_database():
    con = sqlite3.connect(database='database/ims.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT,name text,password text,address text)")
    con.commit()




    con.close()
    
create_database()