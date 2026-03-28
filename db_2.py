import sqlite3
try:
    connection = sqlite3.connect('MY_DATABASE.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS MY_TABLE(
    ido integer PRIMARY KEY,
    name text,
    age integer,
    review text,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    connection.commit()
    connection.close()
except sqlite3.OperationalError:
    print('שגיאה תפעולית')
except sqlite3.IntegrityError as e:
    print(e)
except sqlite3.ProgrammingError:
    print('שגיאת תכנות')
except sqlite3.DatabaseError:
    print('שגיאה במסד הנתונים')
except sqlite3.Error as v:
    print(v)
except sqlite3.Exception as s:
    print(s)
