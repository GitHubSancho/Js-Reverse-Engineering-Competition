#!/usr/bin/env python
#-*- coding: utf-8 -*-
#FILE: js12.py
#CREATE_TIME: 2022-10-09
#AUTHOR: Sancho

import requests
import base64


def build_m(num):
    # 字符串组合
    _str = f'yuanrenxue{num}'
    # 对字符串转换成ASCLL码
    _str = _str.encode('utf-8')
    # 返回url编码的数据
    return base64.b64encode(_str).decode('utf-8')


def build_params(num):
    num = str(num)
    return {'page': num, 'm': build_m(num)}


def count_num():
    nums = []
    url = 'https://match.yuanrenxue.com/api/match/12'

    for n in range(1, 6):
        params = build_params(n)
        resp = session.get(url=url,
                           params=params,
                           headers=headers,
                           cookies=cookies)
        nums.extend(v['value'] for v in resp.json()['data'])
    return sum(nums)


def commit(num):
    url = "https://match.yuanrenxue.com/api/answers"
    params = {'answer': num, 'id': 12}
    resp = session.get(url, params=params, cookies=cookies)
    print(resp.json())


if __name__ == '__main__':
    session = requests.Session()
    headers = {"user-agent": "yuanrenxue.project"}
    # 注意更改sessionid
    cookies = {'sessionid': 'aqik06jitjygpspe53maba72oifwhoqy'}
    # 求和
    num = count_num()
    print(num)
    # 提交答案
    commit(num)
"""
405582
{'user': 'sancho', 'info': 'success', 'status_code': '1'}
"""