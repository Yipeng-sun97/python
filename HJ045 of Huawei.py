'''
描述

给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。 
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个字符串，计算每个字符串最大可能的“漂亮度”。
'''
示例1

输入：
2
zhangsan
lisi

输出：
192
101

说明：
对于样例lisi，让i的漂亮度为26，l的漂亮度为25，s的漂亮度为24，lisi的漂亮度为25+26+24+26=101.   


####solution#####
import sys


def func(s):
    dic = {}
    for i in s:
        dic[i] = s.count(i)
    dic = sorted(dic.items(), key=lambda x: -x[1])

    n = len(dic)
    num = []
    score = 26
    for i in range(n):
        num.append(score)
        score -= 1
    res = 0
    for i in range(n):
        res += dic[i][1] * num[i]
    print(res)
    
while True:
    try:
        n=int(input())
        for i in range(n):
            s=input()
            func(s)
    except:
        break
