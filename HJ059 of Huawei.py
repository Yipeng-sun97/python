'''
描述

找出字符串中第一个只出现一次的字符
'''

输入描述：
输入一个非空字符串

输出描述：
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入：
asdfasdfo
输出：
o

######solution#####
import sys
from collections import Counter

s=input()
dic=Counter(s)
for k,v in dic.items():
    if v==1:
        print(k)
        break
else:
    print(-1)
