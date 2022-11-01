from pyqiwip2p import QiwiP2P
from pyqiwip2p.types import QiwiCustomer, QiwiDatetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
#ВОТ
#   ЭТО
#       НЕДОРАЗВИТЫЙ
#                   КИВИ
#           _____   _____
#          /     \ /     \
#         |               |
#         |               | 
#          \             /
#           \           /
#             \_______/  
#
######   ####   ######
#####   ######   #####
####   ##  ###   #####
####   ##  ###   #####
###   ##  ###   ######
##   ##  ###   #######
#   ##  ##   #########
#ХОТЬ И НЕ ДОРАЗВИТЫЙ НО МЫ ЛЮБИМ ЭТУ АВТООПЛАТУ









import random

p2p = QiwiP2P(auth_key="85a78d85afc55f9690f3b34a690e0a84", default_amount=200)

async def billing_site(bot, user_id):
    amount = 1 # Сумма 1 рубль
    lifetime = 15 # Форма будет жить 15 минут
    comment = 'Купить гараж(бомжи)' # Комментарий
    bill = p2p.bill() # Выставление счета
    inline_btn_start = InlineKeyboardButton('Проверить оплату', callback_data=f'check {str(bill.bill_id)}')
    print(bill.bill_id)
    for_add = InlineKeyboardMarkup().add(inline_btn_start)
    text = f'Сумма: {amount}\nСсылка живет: {lifetime} минут\nСсылка:\n{bill.pay_url}' # Отправляем ссылку человеку
    await bot.send_message(user_id, str(text), reply_markup=for_add)

async def check(bot, user_id, bill_id):
    status = p2p.check(bill_id=bill_id).status # bill_id - номер платежа
    print(str(status))
    if status == 'PAID': # Если статус счета оплачен (PAID)
        await bot.send_message(user_id, "Оплата пришла")
    else: # В другом случае
        await bot.send_message(user_id, "Оплата пришла")