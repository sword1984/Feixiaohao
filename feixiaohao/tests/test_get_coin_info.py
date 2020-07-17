#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 5:57
# @Author  : Sword
# @Site    : 
# @File    : test_get_coin_info.py
# @Software: PyCharm

from feixiaohao.api import *

print(len(get_code()))
result = get_coin_info('mixmarvel')

for key, value in result.items():
    print(key, value)