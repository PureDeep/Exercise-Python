'''
Author: PureDeep
Date: 2020-09-28 09:27:25
LastEditors: PureDeep
LastEditTime: 2020-09-28 10:16:11
FilePath: \05-Python\08-docStrings.py
'''
#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def printMax(x, y):
    '''打印两个数中的最大值。
    两个数都必须是整型数'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, '最大')
    else:
        print(y, '最大')

printMax(3,5)
print(printMax.__doc__)