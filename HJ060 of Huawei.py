'''
描述

任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

输入描述：
输入一个大于2的偶数

输出描述：
从小到大输出两个素数
'''
示例1
输入：
20
输出：
7
13

示例2
输入：
4
输出：
2
2

######solution#####
import sys

while True:
    try:
        n=int(input())
        num=[]
        for i in range((n//2),1,-1):
            for j in range(2,i):
                if i%j==0 or (n-i)%j==0:
                    break
            else:
                num.append(i)
                num.append(n-i)
                break
        for i in num:
            print(i)
    except:
        break
