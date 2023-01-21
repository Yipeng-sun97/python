'''
描述

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

输入n，请输出n以内(含n)完全数的个数。
'''
示例1

输入：
1000

输出：
3

######solution####
import sys

n=int(input())
res=[]
for i in range(1,n):
    p=0
    for j in range(1,i):
        if i%j==0:
            p+=j
    if i==p:
        res.append(i)
print(len(res))
