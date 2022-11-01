








#Тоже не трогай, это возможно на будущее











import json
import random

def normalize(phone):
    if phone[0] == "+":
        phone = phone[1:]
    return phone

def normalize9(phone):
    if phone[0] == "7":
        phone = phone[1:]
    return phone

def normalize8(phone):
    if phone[0] == "7":
        phone = "8" + phone[1:]
    return phone

def plusnumber(phone):
    phone = "+"+phone
    return phone

def transformPhone(phone, i):
    if i == 5:
        return '+' + phone[0] + ' (' + phone[1:4] + ') ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]

def transformPhone2(phone):
    return phone[1:4] + ' ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]

def transformPhone1(phone):
    return '+' + phone[0] + ' ' + phone[1:4] + ' ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]
#======================->
mails = (
    "mail.ru",
    "inbox.ru",
    "list.ru",
    "bk.ru",
    "ya.ru",
    "yandex.com",
    "yandex.ua",
    "yandex.ru",
    "gmail.com"
)

def get_service_by_id(list, number):
    return list[number]

def random_service(list):
    return random.choice(list)

def random_name():
    with open("./_subfiles/json/names.json", 'r') as names:
        names = json.load(names)["names"]
    return random.choice(names)

def random_suffix(int_range = 4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)

def random_email():
    return random_name() + random_suffix() + "@" + random.choice(mails)

def random_password():
    return random_name() + random_suffix(int_range = 10)

def random_useragent():
    with open("./_subfiles/json/user_agents.json", 'r') as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)