'''
描述

给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
'''
示例1

输入：
3
0
fang 90
yang 50
ning 70

输出：
fang 90
ning 70
yang 50

#######solution ########
n, rank = int(input()), int(input())
s = [input().split() for i in range(n)]
s = sorted(s, key = lambda x : -int(x[1]), reverse=rank)
for i in s:
    print(i[0], i[1])
    
#####solution####
import sys

n=input()
sign=int(input())
att=[]
for i in range(int(n)):
    s=input().split()
    att.append(s)
att=sorted(att,key=lambda x:-int(x[1]),reverse=sign) #sorted排序函数的功能。
for i in range(int(n)):
    print('{} {}'.format(att[i][0],att[i][1]))
    
    
    
