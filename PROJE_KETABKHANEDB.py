import sqlite3
conn=sqlite3.connect("KETABKHANE.DB")
cursor=conn.cursor()
def SELECT_BOOK():
    A=cursor.execute("SELECT*FROM BOOK")
    conn.commit()
    print(A.fetchall())
def library():
    cursor.execute('''CREATE TABLE IF NOT EXISTS BOOK(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   AUTHOR VARCHAR(50) NOT NULL,
                   BOOK_NAME VARCHAR(20) NOT NULL);''')
    conn.commit()
    cursor.execute('''INSERT INTO BOOK(AUTHOR,BOOK_NAME)
        VALUES
           ("SAADI","GOLESTAN"),
            ("HAFEZ","SGAHNAME"),
            ("ADATHAYE_ATOMI","JAMEZ"),
            ("PEDARE_POOLDAR","RABERT");''')
    conn.commit()
    SELECT_BOOK()
def LOGIN(USER_NAME,PASSWORD):
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR(20) NOT NULL,
        NAME VARCHAR(20) NOT NULL,
        FAMILY VARCHAR(20) NOT NULL,
        PASSWORD VARCHAR(20) NOT NULL);''')
    conn.commit()
    A=cursor.execute('''SELECT * FROM USER WHERE USER_NAME=? AND PASSWORD=?''',(USER_NAME,PASSWORD))
    print(A.fetchone())
    return A.fetchone()
    conn.commit()
def INSERT_USER():
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR(20) UNIQUE NOT NULL,
        NAME VARCHAR(20) NOT NULL,
        FAMILY VARCHAR(20) NOT NULL,
        PASSWORD VARCHAR(20) UNIQUE NOT NULL);''')
    conn.commit()
    cursor.execute('''INSERT INTO USER(USER_NAME,NAME,FAMILY,PASSWORD)
                   VALUES
                   ("UFO","ALI","MHMDI","1111");''')
    conn.commit()


    
