from threading import Thread
from _subfiles.logic.forRU import send_sms
import _subfiles.logic.forUKR
import _subfiles.logic.db_logic__
spamUKR = _subfiles.logic.forUKR.start_spam
db = _subfiles.logic.db_logic__

default_thr = 2

def ru_spam(user_id, clear_phone, name, surname, patronymic, latin_name, email, password, useragent, i, z, proxy):
    db.add_thr(user_id, "False")
    if db.check_thr(user_id) == "False":
        db.set_thr_stat(int(user_id), "True")
        for _ in range(int(default_thr)):
            print("111")
            Thread(target=send_sms, args=(user_id, clear_phone, name, surname, patronymic, latin_name, email, password, useragent, i, z, proxy,)).start()
    
    else:        
        print("LOX")

def ukr_spam(user_id,phone):
    db.add_thr(user_id, "False")
    if db.check_thr(user_id) == "False":
        db.set_thr_stat(int(user_id), "True")
        for _ in range(int(default_thr)):
            print("111")
            Thread(target=spamUKR, args=(str(user_id), str(phone),), daemon=True, name= "thr_"+str(user_id)).start()
    
    else:        
        print("LOX")