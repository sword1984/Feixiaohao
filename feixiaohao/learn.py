#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 5:17
# @Author  : Sword
# @Site    : 
# @File    : learn.py
# @Software: PyCharm

import csv


with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        print(row)

print('-' * 88, end='\n')

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row)

print('-' * 88, end='\n')

# Example of reading tab-separated values
with open('stocks.csv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # Process row
        print(row)
