"""
cron: 0 10 0 ? * *
new Env('光速云签到');
"""
import requests
from ql_api import get_envs

# 登录函数
def login(email,passwd):
    url = 'https://guangsu.buzz/auth/login'
    headers = {
        "Host": "guangsu.buzz",
        "Connection": "keep-alive",
        "Content-Length": "50",
        "sec-ch-ua": "'Chromium';v='110', 'Not A(Brand';v='24', 'Microsoft Edge';v='110'",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"
    }

    data = f"email={email}&passwd={passwd}&code="
    res = requests.post(url=url,headers=headers,data=data)
    try :
        if res.json()["ret"] == 1:
            return res
        else:
            print(res.json()["msg"])
            return res.json()["msg"]
    except:
        print(res.text)
        return res.text

# 获取cookies
def get_cookies(res):
    try:
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        return cookie["uid"],cookie["email"],cookie["key"],cookie["ip"],cookie["expire_in"]
    except:
        return False

# 签到函数
def checkin(uid, email, key, ip, expire_in):
    url = "http://guangsu.buzz/user/checkin"
    headers = {
        "Host": "guangsu.buzz",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46",
        "X-Requested-With": "XMLHttpRequest"
    }
    cookies = {
        "uid" : uid,
        "email": email,
        "key": key,
        "ip": ip,
        "expire_in": expire_in
    }
    res = requests.post(url,headers=headers,cookies=cookies)
    try:
        print(res.json()["msg"])
    except:
        print(res.text)

if __name__ == "__main__":
    checkin(*get_cookies(login(*get_envs("AIRPORT_ACCOUNT")[0]["value"].split(","))))
