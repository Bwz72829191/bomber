

#ПРОЖУ ИГРАЙСЯ ТУТ ТОЛЬКО С ТЕКСТОМ А ТО ЗАЕБУСЬ ИСПРАВЛЯТЬ


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import re
import requests
import json
import random
import iuliia
from fake_useragent import UserAgent
#---------------------------------
import _subfiles.logic.send_request
import _subfiles.logic.db_logic__
import _subfiles.logic.qiwi_all
from _subfiles.logic.starts import ru_spam, ukr_spam
from _subfiles.logic.proxy_grabber import grab_new_proxy
#from _subfiles.logic.starts import *

_subfiles.logic.db_logic__.create_table()
_subfiles.logic.db_logic__.create_spammer()
_subfiles.logic.db_logic__.add_user("", "liprikon65877", "Admin")

db = _subfiles.logic.db_logic__
qiwit = _subfiles.logic.qiwi_all
check_us = _subfiles.logic.db_logic__.check_stat
check_lic = _subfiles.logic.db_logic__.check_license
req = _subfiles.logic.send_request
#---------------------------------
PRICE = 199 # Сумма 1 рубль
QIWI_TOKEN = '7ebc90039a5e2b606fbd4fdbe0da312c' # api ключ для работы с QIWI
QIWI_ACCOUNT = '79670347414' # номер телефона qiwi

botname = "ddb_search_telegrambot"
Nchannel = "Поиск людей"
NchannelID = 1175675749

TOKEN = "5639410858:AAFuaxEhxBeI90ppLZhPDOIhh6zP_MNaBXs"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#---------------------------------

def generate_credentials():

		vocabulary = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

		name_vocabulary = [
		'Павел', 'Михаил', 'Иван', 'Матвей', 'Игорь', 'Владимир',
		'Михаил', 'Георгий', 'Савелий', 'Никита', 'Александр', 
		'Алексей', 'Роман', 'Марк', 'Макар', 'Егор', 'Тихон',
		'Андрей', 'Родион', 'Максим', 'Даниил', 'Кирилл', 'Лев', 
		'Тимофей', 'Степан'
		]

		surname_vocabulary = [
		'Смирнов', 'Яковлев', 'Воробьев', 'Фомин', 'Миронов',
		'Капустин', 'Соболев', 'Захаров', 'Акимов', 'Кравцов',
		'Алексеев', 'Александров', 'Романов', 'Бочаров', 'Павлов',
		'Новиков', 'Афанасьев', 'Колосов', 'Антонов', 'Денисов',
		'Зубков', 'Мещеряков', 'Андреев'
		]

		patronymic_vocabulary = [
		'Артёмович', 'Александрович', 'Леонидович', 'Георгиевич',
		'Андреевич', 'Игоревич', 'Максимович', 'Романович', 
		'Давидович', 'Викторович', 'Егорович', 'Олегович',
		'Сергеевич', 'Фёдорович'
		]

		email_vocabulary = [
		'gmail.com', 'yandex.ru', 'ya.ru', 'bk.ru', 'mail.ru',
		'yahoo.com', 'list.ru', 'ya.kz', 'yandex.ua', 'ya.ua',
		'yandex.kz', 'ya.kz', 'inbox.ru','internet.ru', 'inbox.ru',
		'yandex.by', 'ya.by'
		]

		password = ''
		for x in range(12):
			password += random.choice(vocabulary)

		rand_end = random.randint(1, 3)

		# randomizing the ending of email, 1 - just random number, 2 - random full year, 3 - random shortened year
		if rand_end == 1:
			rand_end = random.randint(500, 999)
		elif rand_end == 2:
			rand_end = random.randint(1965, 1999)
		else:
			rand_end = str(random.randint(1965, 1999))[2:]

		# random separator
		# write name_surname or namesurname or name-surname (underscore True or False)
		rand_sep = random.randint(1, 3)
		if rand_sep == 1:
			rand_sep = '_'
		elif rand_sep == 2:
			rand_sep = '-'
		else:
			rand_sep = ''

		# using yandex maps transliteration schema as default
		yandex_maps = iuliia.Schemas.get("yandex_maps")

		name = random.choice(name_vocabulary)
		latin_name = iuliia.translate(name, schema = yandex_maps)

		surname = random.choice(surname_vocabulary)
		latin_surname = iuliia.translate(surname, schema = yandex_maps)

		patronymic = random.choice(patronymic_vocabulary)

		email_value = latin_name.lower() + rand_sep + latin_surname.lower() + str(rand_end)

		email = "{}@{}".format(email_value, random.choice(email_vocabulary))

		return name, surname, patronymic, latin_name, email, password

async def check_string(string, user_id):
        phone = re.sub(r'\b\D', '', string)
        clear_phone = re.sub(r'[\ \(]?', '', phone)
        if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',string):
            if int(clear_phone) > 79000000000 and int(clear_phone) < 79999999999 or int(clear_phone) > 89000000000 and int(clear_phone) < 89999999999:
                if int(clear_phone) > 89000000000 and int(clear_phone) < 89999999999:
                    clear_phone = int(clear_phone) - 10000000000
                try:
                    clear_phone = clear_phone.replace("+","")
                except:
                    pass
                if db.check_thr(user_id) != "True":
                    creds = generate_credentials()
                    proxy = ''
                    name = creds[0]
                    surname = creds[1]
                    patronymic = creds[2]
                    latin_name = creds[3]
                    email = creds[4]
                    password = creds[5]
                    
                    ua = UserAgent()
                    useragent = ua.random
                    
                    lines = list(open('./_subfiles/proxy/proxy.txt', 'r'))
                    proxies = []
                    
                    for i in lines:
                        proxies.append(i.replace('\n', ''))
                    
                    z = random.choice(proxies)
                    proxies = {'http': "http://{}".format(z), 'https':"http://{}".format(z)}
                    
                    ru_spam(user_id, str(clear_phone), name, surname, patronymic, latin_name, email, password, useragent, 1, z, proxies)
                    text = "[---|"+str(clear_phone)+"|---]" + " \nСпам запущен![Ру]"
                else:
                    text = "[---|"+str(clear_phone)+"|---]" + " \nОстановите спам для запуска!"
                await bot.send_message(user_id, str(text))
                return(True)
        else: 
            return(False)   

async def check_string_ukr(string, user_id):
        phone = re.sub(r'\b\D', '', string)
        clear_phone = re.sub(r'[\ \(]?', '', phone)
        if re.findall(r'^[\+380|380]*?\d{12}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',string):
            try:
                clear_phone = clear_phone.replace("+","")
            except:
                pass
            if db.check_thr(user_id) != "True":
                ukr_spam(user_id, clear_phone)
                text = "[---|"+str(clear_phone)+"|---]" + " \nСпам запущен![Укр]"
            else:
                text = "[---|"+str(clear_phone)+"|---]" + " \nОстановите спам для запуска!"
            await bot.send_message(user_id, str(text))
            return(True)
        else: 
            return(False)   

def inline_keyboard(why, user_id = None):
    print(str(user_id))
    if why == "check_by_admin":
        inline_btn_start_last = InlineKeyboardButton('❓Проверить оплату❓', callback_data=f'license {str(user_id)}')
        for_add = InlineKeyboardMarkup().add(inline_btn_start_last)
    if why == "adduser" and user_id != None:
        inline_btn_add_yes = InlineKeyboardButton('Да', callback_data=f'add {str(user_id)}')
        inline_btn_add_no = InlineKeyboardButton('Нет', callback_data=f'no {str(user_id)}')
        for_add = InlineKeyboardMarkup().add(inline_btn_add_yes, inline_btn_add_no)
    if why == "instruction_start":
        inline_btn_start = InlineKeyboardButton('Лицензионное соглашение', callback_data=f'license1 {str(user_id)}')
        for_add = InlineKeyboardMarkup().add(inline_btn_start)
    if why == "soglasen":
        inline_btn_start_last = InlineKeyboardButton('❓Оплатить❓', callback_data=f'true {str(user_id)}')
        for_add = InlineKeyboardMarkup().add(inline_btn_start_last)
    return for_add

def keybaord_all(type_k):
    markup_big = ReplyKeyboardMarkup(resize_keyboard=True)
    if type_k == "user":
        markup_big.row("🔥ЗАХУЯРИТЬ🔥","!СТОП!")
        markup_big.row("🇺🇦УКРАИНА🇺🇦", "🇷🇺РОССИЯ🇷🇺")
        markup_big.row("Послать нахуй", "(◕‿◕)")
    if type_k == "admin_usr":
        markup_big.row("🔥ЗАХУЯРИТЬ🔥","!СТОП!")
        markup_big.row("🇺🇦УКРАИНА🇺🇦", "🇷🇺РОССИЯ🇷🇺")
        markup_big.row("Послать нахуй", "(◕‿◕)")
        markup_big.row("┼Адм.Меню┼")
    if type_k == "admin":
        markup_big.row("┼ИНФОРМАЦИЯ╤", "╤ПОМОЩЬ┼")
        markup_big.row("┼Обновить прокси┼")
        markup_big.row("┼Вернуться┼")
    return markup_big

def check__system__all__and__blyat__users():
    user_count = _subfiles.logic.db_logic__.count_users()
    thr_count = _subfiles.logic.db_logic__.count_start_thread()
    text_simple = f"╒Кол-во пользователей [{str(user_count)}]\n╒Кол-во запущенных спамов [{str(thr_count)}]"
    return text_simple

async def check_suka(codd, bot):
        cod = code[1]
        aaaa = 0
        hui = 1
        h = requests.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments?rows=30',
                                                                            headers={'Accept': 'application/json',
                                                                                    'Content-Type': 'application/json',
                                                                                    'Authorization': f'Bearer {QIWI_TOKEN}'})
        req = json.loads(h.text)
        for i in range(len(req['data'])):
            if req['data'][i]['comment'] == f"{cod}":
                if req['data'][i]['sum']['amount'] == PRICE:
                    aaaa = 1
                    _subfiles.logic.db_logic__.set_status(str(code[1]), "User")
                    await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = f"Платеж получен!\nНапишите /start если кнопки не появились") 
                    
                    await bot.send_message(NchannelID, f"Покупка\nСумма: {PRICE}р\nBOMJ_BOMER")         
                    await bot.send_message(chat_id = code[1], text="А вот и кнопочки <3", reply_markup=keybaord_all("user"))
                else: # В другом случае
                    try:
                        if aaaa != 1:
                            await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = f'Счет\nНЕ ОПЛАЧЕН→→→\n\nПополнение счета на сумму: {PRICE}.'
                                                                                                                            f'\n\nОплатите счет по номеру QIWI: {QIWI_ACCOUNT}.'
                                                                                                                                f'\nВ комментарий к оплате оставьте: {cod}.',reply_markup=inline_keyboard("check_by_admin", str(code[1])))
                    except:
                        pass
        


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    #code_s = callback_query.data.lower()
    
    code = callback_query.data.split(" ")
    if code[0] == "true":
        await bot.send_message("eblan", f"Написал новый пользователь с нажатием на *Оплатить*")
        cod = code[1]
        
        db.set_qiwi_code(callback_query.message.chat.id, str(code))
        await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = f'Счет\n\nПополнение счета на сумму: {PRICE}.'
                                                                                                                                    f'\n\nОплатите счет по номеру QIWI: {QIWI_ACCOUNT}.'
                                                                                                                                    f'\nВ комментарий к оплате оставьте: {cod}.',reply_markup=inline_keyboard("check_by_admin", str(code[1])))
    elif code[0] == "license":
        await check_suka(codd, bot)
                                                                                                                                         
    elif code[0] == "adding":
        _subfiles.logic.db_logic__.set_license(str(code[1]), "Gay")
        await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = "-_-_-_-_-_-_-_-_-_-_-_-_-")
        await bot.send_message(chat_id = code[1], text="А вот и кнопочки <3", reply_markup=keybaord_all("user"))
    elif code[0] == "add":
        _subfiles.logic.db_logic__.set_status(str(code[1]), "User")
        await bot.send_message(chat_id = code[1], text="Вы были добавленны админом!\nНапишите /start что-бы продолжить.")
        await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = f"Вы добавили {str(code[1])}")
    elif code[0] == "no":
        await bot.send_message(chat_id = code[1], text="Вы были отклонены от добавления в бота.")
        await bot.edit_message_text(chat_id = callback_query.message.chat.id, message_id = callback_query.message.message_id,text = f"Вы не добавили пользователя...")

@dp.message_handler(commands=['spam'])
async def set_spam(message: types.Message):
    user_id = message.chat.id
    print(user_id)
    if user_id != "":
        _subfiles.logic.db_logic__.set_status(user_id, "Spam")
        await bot.send_message(message.chat.id, "Все у вас статус спаммера!", reply_markup=keybaord_all("spammer"))
    else:
        await bot.send_message(message.chat.id, "Переделывай долбоеб")
@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    f_name = message.chat.first_name
    user_id = message.chat.id
    username = message.chat.username
    def check_user(chat_id):
        chat_ids_file = 'chat_ids.txt'
        with open(chat_ids_file, "a+") as ids_file:
            ids_file.seek(0)
            ids_list = [line.split('\n')[0] for line in ids_file]
        if str(chat_id) in ids_list:
            user_in_base = True
        else:
            user_in_base = False
        return user_in_base

    if check_user(message.chat.id) != True:
        try:
            _subfiles.logic.db_logic__.add_user(str(user_id), str(username), "Free", whoInvate = str(message.text.split(" ")[1]))
            print(message.text)
        except:
            _subfiles.logic.db_logic__.add_user(str(user_id), str(username), "Free")
    else:
        _subfiles.logic.db_logic__.add_user(str(user_id), str(username), "User")
    if check_us(str(user_id)) == "Admin":
        await bot.send_message(user_id, f"{f_name} ну да блять админ\nзагрузка... ██████████████] 99.9%\n✺◟( ͡° ͜ʖ ͡°)◞✺ Не дал админу умереть с голода\n♡´･ᴗ･`♡ поэтому держи от нас презент бомбер для бомжей\n° ͜ʖ ͡ - уничтожай телефоны элиты", reply_markup=keybaord_all("admin_usr"))
    if check_us(str(user_id)) == "User":
        await bot.send_message(user_id, f"{f_name} ну да блять\nзагрузка... ██████████████] 99.9%\n✺◟( ͡° ͜ʖ ͡°)◞✺ Не дал админу умереть с голода\n♡´･ᴗ･`♡ поэтому держи от нас презент бомбер для бомжей\n° ͜ʖ ͡ - уничтожай телефоны элиты", reply_markup=keybaord_all("user"))
    
    if check_us(str(user_id)) == "Spam":
        await bot.send_message(user_id, f"{f_name} для вас доступна только реферальная ссылка, в будущем добавлю функционал бомбера.", reply_markup=keybaord_all("spammer"))
    if check_us(str(user_id)) == "Free":
        #await qiwit.billing_site(bot, user_id) !!!!!!!!!!!!!!!!!!!!!!НЕ ТРОГАТЬ!!!!!!!!!!!!!!!!! БУДУЩИЙ КИВИ, ОН НЕДОРАЗВИТЫЙ ПОКАЧТО !!!!!!!!!!!!!!!!!!!!!!!!!!!!ПОНЯЛ МЕНЯ???? КИВИ НЕ ТРОГАТЬ!!!!!!!!!!!!!!1
        status = f"Здравствуйте, у вас нет доступа!\n!СЕГОДНЯ ДЕЙСТВУЕТ СКИДКА!\nСтоимость lifetime подписки {PRICE}\nНажмит кнопку снизу чтобы приступить к оплате!"
        await bot.send_message(user_id, status, reply_markup=inline_keyboard("soglasen", user_id))

@dp.message_handler(commands=['setadm'])
async def set_admin(message: types.Message):
    user_id = message.chat.id
    if check_us(str(user_id)) == "Admin":
        user_id = str(message.text).replace("/setadm ", "")
        print(user_id)
        if user_id != "":
            _subfiles.logic.db_logic__.set_status(user_id, "Admin")
            await bot.send_message(message.chat.id, "Все пидор теперь админ")
        else:
            await bot.send_message(message.chat.id, "Переделывай долбоеб")

@dp.message_handler(commands=['setusr'])
async def set_user(message: types.Message):
    user_id = message.chat.id
    if check_us(str(user_id)) == "Admin":
        user_id = str(message.text).replace("/setusr ", "")
        print(user_id)
        if user_id != "":
            _subfiles.logic.db_logic__.set_status(user_id, "User")
            await bot.send_message(message.chat.id, "Все пидор теперь админ")
        else:
            await bot.send_message(message.chat.id, "Переделывай долбоеб")

@dp.message_handler(content_types=["text"])
async def pizdec(message: types.Message):
    user_id = message.chat.id
    #username = message.chat.username
    f_name = message.chat.first_name
    #l_name = message.chat.last_name
    if check_us(str(user_id)) == "Admin":
        if await check_string(message.text, user_id):
            pass
        elif await check_string_ukr(message.text, user_id):
            pass
        else:
            if message.text == "🔥ЗАХУЯРИТЬ🔥":
                await bot.send_message(user_id, f"УРА МЫ СКАКНУЛИ ДАЛЬШЕ!!\nТеперь тестируем чистку номера\nВводим хоть как\n+7(999)000000\n+7(999 0-00-00-0\nТестируем систему(буквы сука не считаются!)\nС УКР тоже работает!")
            elif message.text == "🇺🇦УКРАИНА🇺🇦":
                await bot.send_message(user_id, f"""██████████████████████████████
██████████████░░██████████████
████░████████░░░░████████░████
████░░░██████░░░░██████░░░████
████░█░░░█████░░██████░░█░████
████░██░░█████░░█████░░██░████
████░███░░████░░████░░███░████
████░███░░████░░████░░███░████
████░███░░████░░████░░███░████
████░████░░███░░███░░████░████
████░████░░███░░███░░████░████
████░██░░░███░░░░███░░░██░████
████░██░░███░░██░░███░░██░████
████░██░░░██████████░░░██░████
████░████░░░░░██░░░░░████░████
████░█████░░██░░██░░█████░████
████░░░░░░░░░░░░░░░░░░░░░░████
██████████░░██░░██░░██████████
░██████████░░█░░█░░██████████
░░██████████░░░░░░██████████
░░░░█████████░░░░█████████
░░░░░░░░██████████████
░░░░░░░░░░░░░████""")
            elif message.text == "🇷🇺РОССИЯ🇷🇺":
                await bot.send_message(user_id, f"""░░░░░░░░░░░░░╬░░░░░░░░░░░░░
░░░░░░░░░░░█▄█▄█░░░░░░░░░░░
░░░░░░░░░▄░▄███▄░▄░░░░░░░░░
░░░░░░▄████▄░░░▄████▄░░░░░░
░░░▄██▄░░░██▄▄▄██░░░▄██▄░░░
░░▄█████░░███████░░█████▄░░
░▄███████████████████████▄░
░█████████████████████████░
░█████▀▀▀█████████▀▀▀█████░
░░██▀░░░▄█████████▄░░░▀██░░
░░░░▀██▀░░▄█████▄░░▀██▀░░░░
░░░░░░▀░░▄███████▄░░▀░░░░░░
░░░░░░░░░███▀▀▀███░░░░░░░░░
░░░░░░░░░█▀░░░░░▀█░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
            elif message.text == "Послать нахуй":
                await bot.send_message(user_id, f"大 Пошла нахуй,пидарасина ๏̯͡๏")
            elif message.text == "!СТОП!":
                db.set_thr_stat(int(user_id), "False")
                await bot.send_message(user_id, f"Потоки сейчас будут остановлены!")
            elif message.text == "(◕‿◕)":
                await bot.send_message(user_id, f"♥️ I ℓ٥ﻻ ﻉ√٥υ ♥️")
            elif message.text == "┼Адм.Меню┼":
                await bot.send_message(user_id, f"{f_name}, добро пожаловать в админку", reply_markup=keybaord_all("admin"))
            elif message.text == "┼ИНФОРМАЦИЯ╤":
                info_text = check__system__all__and__blyat__users()
                await bot.send_message(user_id, f"{str(info_text)}")
            elif message.text == "╤ПОМОЩЬ┼":
                await bot.send_message(user_id, f"-/setadm [id] - добавить админа")
            elif message.text == "┼Обновить прокси┼":
                grab_new_proxy(user_id)
                await bot.send_message(user_id, f"{f_name}, поверь прокси обновляются...\nВывод тяжело сделать пахзпазхапхз")
            elif message.text == "┼Вернуться┼":
                await bot.send_message(user_id, f"{f_name}, возвращайся в нечтожный мир", reply_markup=keybaord_all("admin_usr"))
            
    if check_us(str(user_id)) == "User":
        if await check_string(message.text, user_id):
            pass
        elif await check_string_ukr(message.text, user_id):
            pass
        else:
            if message.text == "🔥ЗАХУЯРИТЬ🔥":
                await bot.send_message(user_id, f"УРА МЫ СКАКНУЛИ ДАЛЬШЕ!!\nТеперь тестируем чистку номера\nВводим хоть как\n+7(999)000000\n+7(999 0-00-00-0\nТестируем систему(буквы сука не считаются!)\nС УКР тоже работает!")
            elif message.text == "!СТОП!":
                db.set_thr_stat(int(user_id), "False")
                await bot.send_message(user_id, f"Потоки сейчас будут остановлены!")
            elif message.text == "🇺🇦УКРАИНА🇺🇦":
                await bot.send_message(user_id, f"""██████████████████████████████
██████████████░░██████████████
████░████████░░░░████████░████
████░░░██████░░░░██████░░░████
████░█░░░█████░░██████░░█░████
████░██░░█████░░█████░░██░████
████░███░░████░░████░░███░████
████░███░░████░░████░░███░████
████░███░░████░░████░░███░████
████░████░░███░░███░░████░████
████░████░░███░░███░░████░████
████░██░░░███░░░░███░░░██░████
████░██░░███░░██░░███░░██░████
████░██░░░██████████░░░██░████
████░████░░░░░██░░░░░████░████
████░█████░░██░░██░░█████░████
████░░░░░░░░░░░░░░░░░░░░░░████
██████████░░██░░██░░██████████
░██████████░░█░░█░░██████████
░░██████████░░░░░░██████████
░░░░█████████░░░░█████████
░░░░░░░░██████████████
░░░░░░░░░░░░░████""")
            elif message.text == "🇷🇺РОССИЯ🇷🇺":
                await bot.send_message(user_id, f"""░░░░░░░░░░░░░╬░░░░░░░░░░░░░
░░░░░░░░░░░█▄█▄█░░░░░░░░░░░
░░░░░░░░░▄░▄███▄░▄░░░░░░░░░
░░░░░░▄████▄░░░▄████▄░░░░░░
░░░▄██▄░░░██▄▄▄██░░░▄██▄░░░
░░▄█████░░███████░░█████▄░░
░▄███████████████████████▄░
░█████████████████████████░
░█████▀▀▀█████████▀▀▀█████░
░░██▀░░░▄█████████▄░░░▀██░░
░░░░▀██▀░░▄█████▄░░▀██▀░░░░
░░░░░░▀░░▄███████▄░░▀░░░░░░
░░░░░░░░░███▀▀▀███░░░░░░░░░
░░░░░░░░░█▀░░░░░▀█░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
            elif message.text == "Послать нахуй":
                await bot.send_message(user_id, f"大 Пошла нахуй,пидарасина ๏̯͡๏")
            elif message.text == "(◕‿◕)":
                await bot.send_message(user_id, f"♥️ I ℓ٥ﻻ ﻉ√٥υ ♥️")
    if check_us(str(user_id)) == "Free":
        status = f"Здравствуйте, у вас нет доступа!\nСтоимость lifetime подписки {PRICE}\nНажмит кнопку снизу чтобы приступить к оплате!"
        await bot.send_message(user_id, status, reply_markup=inline_keyboard("soglasen", user_id))

if __name__ == '__main__':
    executor.start_polling(dp)
