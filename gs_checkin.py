"""
cron: 0 10 0 ? * *
new Env('光速云签到');
"""

import requests
from gs_login import login,get_cookies
from ql_api import get_envs

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
