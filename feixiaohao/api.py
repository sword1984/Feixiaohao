#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 5:01
# @Author  : Sword
# @Site    : 
# @File    : api.py
# @Software: PyCharm


import json
import logging
import requests

def get_code():
    """Get all of the token's code on feixiaohao """

    url = 'https://dncapi.bqiapp.com/api/coin/data_list?webp=1'

    response = requests.get(url=url).json()

    if response['code'] == 200:
        return response['data']
    else:
        raise TypeError


def get_coin_info(code):
    """Get token's information"""

    url = 'https://dncapi.bqiapp.com/api/coin/web-coininfo'
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    payload = {'code': code}
    # Converts a character into a dictionary
    null = None
    true = True

    response = requests.post(url=url, headers=headers,
                             data=json.dumps(payload))

    print(response.json())
    if response.status_code == 200:
        response_dict = eval(response.text)
        return response_dict['data']
    else:
        logging.log(logging.WARNING, 'web-coininfo is error: {}'.format(response.status_code))


if __name__ == '__main__':
    result = get_code()
    import csv
    headers = ['code', 'name', 'name_zh', 'symbol', 'logo', 'type']
    with open('test.csv', 'wt', encoding='utf-8', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(result)

