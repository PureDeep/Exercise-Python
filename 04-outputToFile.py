'''
Author: PureDeep
Date: 2020-09-28 09:10:38
LastEditors: PureDeep
LastEditTime: 2020-09-28 09:12:36
FilePath: \05-Python\04-outputToFile.py
'''
#-*- coding: utf-8 -*-

import sys
f = open('d:/01-Learning/05-Python/test.txt', 'a+')
a = '123'
b = '456'
print(a,b,file=f)
f.close()