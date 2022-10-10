#!/usr/bin/env python
#-*- coding: utf-8 -*-
#FILE: js13.py
#CREATE_TIME: 2022-10-10
#AUTHOR: Sancho

import re
import requests
import execjs

session = requests.Session()

# 模拟第一次请求，获取coockie
url = "https://match.yuanrenxue.com/match/13"
cookies = {"sessionid": "7unvdtil9vz9hnxqmmx9r4qqxj2rxl73"}
resp = session.get(url, cookies=cookies, timeout=9)

# 生成cookie
js_code = resp.text
js_code = re.findall("\(.*/';", js_code)[0]
js_code = js_code.split(';')[0][:-2]  # 去除路径
# 模拟js运行
js_code = f"function result(){{cookie={js_code} ;return cookie}}"
result = execjs.compile(js_code).call('result')
# 格式化参数
result = result.split('=')
r_head = result[0]
r_body = result[1]

# 模拟第二次请求 + 翻页访问
cookies[r_head] = r_body
url = 'https://match.yuanrenxue.com/api/match/13'
session.headers.update({'user-agent': 'yuanrenxue.project'})
data = []
for n in range(1, 6):
    params = {'page': n}
    resp = session.get(url, params=params, cookies=cookies, timeout=9)
    data.append(resp.json())

# 加和计算
values = [v['value'] for j in data for v in j['data']]
count = sum(values)

# 提交答案
params = {'answer': count, 'id': '13'}
url = "https://match.yuanrenxue.com/api/answers"
resp = session.get(url, cookies=cookies, params=params)
print(resp.text)


"""
{"user": "sancho", "info": "success", "status_code": "1"}
"""