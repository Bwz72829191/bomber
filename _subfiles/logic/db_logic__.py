
#　　　　　　　　　　　　　　;' ':;,,　　　 ,;'':;,
#　　　　　　　　　　　　　;'　　 ':;,,.,,;'　　';,
#　　ー　　　　　　　　 ,:'　　　　　　　　::::::::､
#　_＿　　　　　　　　,:' ／ 　 　 　　＼ 　::::::::', Have A Good day
#　　　　　二　　　　:'　 ●　　　　　 ●　 　  ::::::::i.
#　　￣　　　　　　　i　 '''　(__人_)　''''   ::::::::::i
#　　　　-‐　　　　　 :　 　　　　　　　　 　::::::::i
#　　　　　　　　　　　`:,､ 　　　　　 　  :::::::::: /
#　　　　／　　　　　　 ,:'　　　　　　　 : ::::::::::::｀:､
#　　　　　　　　　　　 ,:'　　　　　　　　 : : ::::::::::｀:､

#это sql детка



import random
import sqlite3

name_db = "all_db.db"
name_db_spam = "spam_db.db"

def create_spammer():
    conn = sqlite3.connect(f"_subfiles/DataBase/{name_db_spam}")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS spammers(
                    UserId INT PRIMARY KEY,
                    UserName TEXT,
                    RefID INT,
                    RefNum INT);
                    """)
    conn.commit()

def add_spammer(user_id, username, RefID = str(random.randint(99999,99999999)+228), RefNum = "0"):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db_spam}")
        cur = conn.cursor()

        user = (user_id, username, RefID, RefNum)
        cur.execute("INSERT INTO spammers VALUES(?, ?, ?, ?)", user)
        conn.commit()
        print("Спаммер успешно добавлен!")
    except:
        print("Спаммер уже добавлен!")

def check_count(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db_spam}")
        cur = conn.cursor()
        cur.execute(F"SELECT Type FROM users WHERE UserID=({user_id})")
        cont = cur.fetchone()
        return cont[0]
    except:
        return None

def create_table():
    conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
    cur = conn.cursor()
    #Создаём столбцы ID, UserID, UserName, Type
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    UserId INT PRIMARY KEY,
                    UserName TEXT,
                    Type TEXT,
                    License TEXT,
                    WhoInvate TEXT);
                    """)
    conn.commit()
    #Создаём столбцы ID, UserID, TreadName
    cur.execute("""CREATE TABLE IF NOT EXISTS Thread(
                    UserId INT PRIMARY KEY,
                    ThreadName TEXT);
                    """)
    conn.commit()

def set_qiwi_code(user_id, code_qiwi):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()
        cur.execute(f"UPDATE users SET QIWICode = '{code_qiwi}' WHERE UserId = '{user_id}'")
        conn.commit()
    except:
        pass

def check_qiwi_code(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
        cur = conn.cursor()
        cur.execute(F"SELECT QIWICode FROM users WHERE UserID=({user_id})")
        cont = cur.fetchone()
        return cont[0]
    except:
        return None

def count_users():
    conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
    cur = conn.cursor()
    #Создаём столбцы ID, UserID, UserName, Type
    ocunt = cur.execute("SELECT COUNT(*) FROM users")
    ocunt = cur.fetchall()
    num_of_rows = ocunt[0][0]
    conn.commit()
    return str(num_of_rows)
    
def get_spammers(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
        cur = conn.cursor()
        cur.execute(F"SELECT UserName FROM users WHERE UserID=({user_id})")
        cont = cur.fetchone()
        return cont[0]
    except:
        return "0"

def add_user(user_id, username, status, license_n = "NotGay", whoInvate = "Админ Епта"):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()

        user = (user_id, username, status, license_n, whoInvate)
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", user)
        conn.commit()
        print("Пользователь успешно добавлен!")
    except:
        print("Пользователь уже добавлен!")

def set_license(user_id, status):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()
        cur.execute(f"UPDATE users SET License = '{status}' WHERE UserId = '{user_id}'")
        conn.commit()
        print(f"Статус лицензии пользователя - {status}!")
    except:
        print("Не смогли изменить статус лицензии пользователя!")
    
def set_status(user_id, status):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()
        if user_id != None:
            cur.execute(f"UPDATE users SET Type = '{status}' WHERE UserId = '{user_id}'")
        conn.commit()
        print(f"Пользователю присвоен статус - {status}!")
    except:
        print("Не смогли изменить статус!")

def check_stat(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
        cur = conn.cursor()
        cur.execute(F"SELECT Type FROM users WHERE UserID=({user_id})")
        cont = cur.fetchone()
        return cont[0]
    except:
        return "0"

def check_license(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
        cur = conn.cursor()
        cur.execute(F"SELECT License FROM users WHERE UserID=({user_id})")
        cont = cur.fetchone()
        return cont[0]
    except:
        return None
    
def del_user(user_id):
    conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM users WHERE UserId=({user_id})")
    conn.commit()

def add_thr(user_id, thr_name):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()

        thr = (user_id, thr_name)
        cur.execute("INSERT INTO Thread VALUES(?, ?)", thr)
        conn.commit()
        print("Поток успешно добавлен!")
    except:
        print("У пользователя уже есть активный поток!")

def check_thr(user_id):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
        cur = conn.cursor()
        cur.execute(F"SELECT ThreadName FROM Thread WHERE UserId={user_id}")
        cont = cur.fetchone()
        return cont[0]
    except:
        return "HUi"

def set_thr_stat(user_id, status):
    try:
        conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
        cur = conn.cursor()
        cur.execute(f"UPDATE Thread SET ThreadName = '{status}' WHERE UserId = '{user_id}'")
        conn.commit()
        print(f"Статус потока - {status}!")
    except:
        print("Не смогли изменить статус потока!")

def count_start_thread():
    conn = sqlite3.connect(f"_subfiles/DataBase/{name_db}")
    cur = conn.cursor()
    ocunt = cur.execute("SELECT COUNT(*) FROM Thread WHERE ThreadName = 'True'")
    ocunt = cur.fetchall()
    num_of_rows = ocunt[0][0]
    conn.commit()
    return str(num_of_rows)

def del_thr(user_id):
    conn = sqlite3.connect(f"_subfiles/DataBase/all_db.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM Thread WHERE UserId=({user_id})")
    conn.commit()

#create_table() #----Создание БД
#add_user("888888888", "lolipop2018", "Admin") #Добавление пользователя
#print( check_stat("888888888") ) #проверка статуса пользователя
#del_user("888888888") #удаление пользователя
