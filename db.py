import sqlite3


try:
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    if cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';").fetchone() is None:
        cur.execute("""CREATE TABLE users(
                    id TEXT, 
                    money INT DEFAULT 0 NOT NULL)""")
except:
    print('Failed to initialize DB!')

def does_user_exist(id):
    if cur.execute("SELECT id FROM users WHERE id = %s" % (id)).fetchone() is not None:
        return True
    return False

def create_user(id):
    cur.execute("INSERT INTO users VALUES (%s, 0)" % (id))
    con.commit()