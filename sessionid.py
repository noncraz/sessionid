import requests,os
import threading
from user_agent import generate_user_agent

def h():
    username = input("user : ")
    pas = input("password : ")
    
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '2.4901',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()) ,
        'viewport-width': '809',
        'x-asbd-id': '129477',
        'x-csrftoken': 'xmHxyNUhnRrSp13eJy8vuPPcr0XvUtNZ',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1008158962',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{pas}',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': f'{username}',
    }
    
    k= requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
    co = k.cookies
    coo= co.get_dict()
    tok = coo['csrftoken']
    sid = f"{coo['sessionid']}"
    os.system("clear")
    print(sid)
    Id=input("ur id:")
    token=input("ur token:")
    requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(Id)+"&text="+str(tlg))
h()