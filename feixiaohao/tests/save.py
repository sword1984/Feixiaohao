#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 6:56
# @Author  : Sword
# @Site    : 
# @File    : save.py
# @Software: PyCharm


import time
import csv
from queue import Queue
from feixiaohao.api import *
from concurrent.futures import ThreadPoolExecutor, as_completed

q = Queue()

tokens = get_code()
tokens_info = list()

with ThreadPoolExecutor(max_workers=50) as exector:
    result = list()
    for token in tokens:
        res = exector.submit(get_coin_info, token['code'])
        print(res)
        result.append(res)

    print('-' * 500)
    for future in as_completed(result):
        data = future.result()
        time.sleep(1)
        print(data)
        print('*' * 50)