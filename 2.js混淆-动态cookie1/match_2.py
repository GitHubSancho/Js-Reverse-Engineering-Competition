#!/usr/bin/env python
#-*- coding: utf-8 -*-
#FILE: match_2.py
#CREATE_TIME: 2022-10-21
#AUTHOR: Sancho

import requests
import execjs

headers = {
    "user-agent": "yuanrenxue.project",
}
cookies = {"sessionid": "1hb3d6hetn61jntrffo8fzdu7ru3f37k"}
session = requests.session()
session.headers = headers
session.cookies.update(cookies)

with open('2.js混淆-动态cookie1\match_2.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
func = execjs.compile(js_code)

url = "https://match.yuanrenxue.com/api/match/2"

all_sum = 0
for page in range(1, 6):
    co = {'m': func.call('get_m')}
    session.cookies.update(co)
    params = {
        'page': str(page),
    }
    res = session.get(url, params=params)
    print(res.text)

    for data in res.json()['data']:
        all_sum += data['value']

print('总和:', all_sum)
