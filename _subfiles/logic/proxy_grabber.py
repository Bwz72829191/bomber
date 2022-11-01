







#Ну а тут скажу что это еще старый добрый грабер, но он в тг отсылать не будет инфу(траблы кое-какие)








import datetime
import random
import time
import json
import requests
from threading import Thread
proxies_file = "_subfiles\proxy\proxy.txt"



def get_proxies():
    with open(proxies_file,"a+") as proxy_file:
        proxy_file.seek(0)
        proxy_list = [line.split('\n')[0] for line in proxy_file]
        return  proxy_list

def append_proxy(live: bool, proxy: str):
    if live:
        with open(proxies_file, "a+") as proxy_file:
            proxy_file.write(f'{proxy}\n')
            #proxy_file.append(str(proxy))
            print(f'New proxy saved: {proxy}')
    if not live:
         with open("_subfiles\proxy\dead_proxy.txt", "a+") as proxy_file:
            proxy_file.write(f'{proxy}\n')
            #proxy_file.append(str(proxy))
            print(f'New dead_proxy saved: {proxy}')

def getSites(file='_subfiles\json\sites.json'):
    with open(file, 'r') as sites:
        return json.load(sites)["sites"]

def getDomain(url):
    return url.split('/')[2]

class Sites:
    def __init__(self, sites):
        self.sites = sites
        self.timeout = 10
    def grab(self, chat_id):
        site = self.sites["url"]
        chat_id = chat_id
        print('ProxyGrabber', f"{site}")
        

        proxys = [proxy for proxy in requests.get(
            f"{site}",
            ).text.splitlines()]
            # https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=6000&country=RU&ssl=all&anonymity=all&simplified=true
        [proxys.append(proxy) for proxy in get_proxies()]
        site_url = getDomain(site)
        text = chat_id,f'Сайт {site_url}\nВсего спарсил {len(proxys)} прокси...'
        print('ProxyGrabber', f'Check {len(proxys)} proxys...')

        random.shuffle(proxys)
        live_count = 0
        dead_count = 0
        for proxy in proxys:
            #time.sleep(1)
            try:
                timestamp = datetime.datetime.now().timestamp()
                try:
                    proxy_url = "http://" + proxy
                except TypeError:
                    break

                requests.get('https://www.etm.ru/', timeout=2,
                            proxies=dict(http=proxy_url,
                                        https=proxy_url))
                ping = round((datetime.datetime.now().timestamp() - timestamp) * 1000)
                if ping < 1800:
                    live_count += 1
                    if proxy not in get_proxies():
                        append_proxy(True, proxy)
                    print('ProxyGrabber', f'Find proxy ({live_count}/{dead_count}): {proxy} with ping {ping}ms')
                    #bot.send_message(chat_id,f'Нашел прокси ({live_count}/{dead_count}): {proxy} с пингом {ping}ms')
                    continue
                else:
                    dead_count += 1
                    if proxy in get_proxies():
                        append_proxy(False, proxy)
                    continue

            except (Exception, BaseException, requests.exceptions.ConnectionError):
                dead_count += 1
                if proxy in get_proxies():
                    append_proxy(False, proxy)
                continue
        
        text = f'C сайта {site_url} спарсено {len(proxys)}\nЖивых прокси: {live_count}\nМертвых: {dead_count}'
        return text

def proxy_create(proxy_list):
    proxies = []
    for line in proxy_list:
        proxi = ''.join(line)
        proxi = (''+proxi).split()
        proxies.append(proxi)
    return proxies


def proxy_select(proxies, proxy_type):
    proxy = random.choice(proxies)
    proxy = ''.join(proxy)
    proxy = {proxy_type:proxy}
    return(proxy)
    
def grab_new_proxy(chat_id):
    global i
    sites1 = getSites()
    num_site = 0
    def check_proxy(num_site = num_site, sites = sites1, chat_id = chat_id):
        site = sites[i]
        site = Sites(site)
        site.grab(chat_id)
    for i in range(3):
        t = Thread(target=check_proxy)
        t.start()