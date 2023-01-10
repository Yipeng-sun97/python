'''
描述

查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
'''
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw

输出：
jklmnop
import sys


####solution#####

s=input()
t=input()
#res=0
if len(s)>len(t):
    s,t=t,s
mxlen=0
for l in range(1,len(s)):
    for i in range(0,len(s)-l+1):
        sub=s[i:i+l]
        if sub in t and l>mxlen:
            mxlen=l
            res=sub
print(res)
