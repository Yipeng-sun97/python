'''
描述

验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
'''

示例1

输入：
6

输出：
31+33+35+37+39+41

####solution####
import sys

m = 0
n = int(input())
att = []
for i in range(0, n):     #当n=3的时候，是从奇数中第（1+2）个奇数开始加的
    m += i
for j in range(2 * m + 1, 2 * m + 1 + 2 * n, 2):
    att.append(str(j))

print("+".join(att))

#######solution####
n=int(input())
x=n**2-n+1
list1=[]
for i in range(n):
    list1.append(str(x))
    x+=2
print("+".join(list1))
