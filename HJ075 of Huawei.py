'''
描述

给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
'''

输入描述：
输入两个只包含小写字母的字符串

输出描述：
输出一个整数，代表最大公共子串的长度



输入：
asdfas
werasdfaswer

输出：
6

######solution####
import sys

s=input()
t=input()
if len(s)>len(t):
    s,t=t,s
mx=0
for l in range(1,len(s)+1):
    for i in range(0,len(s)-l+1):
        if s[i:i+l] in t:
            mx=l
            break
print(mx)

######solution#####
a, b = input(), input()
if len(a) > len(b):
    a,b = b,a
    
def get_max_len(a, b):
    for i in range(len(a),0,-1):
        for j in range(0, len(a)-i+1):
            if a[j:j+i] in b:
                return i
    return 0
print(get_max_len(a,b))
