'''
描述

现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：
称重重量包括 0
'''
输入描述：

对于每组测试数据：
第一行：n --- 砝码的种数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
输出描述：

利用给定的砝码可以称出的不同的重量数

示例1

输入：
2
1 2
2 1

输出：
5
复制
说明：
可以表示出0，1，2，3，4五种重量。   

#######solution######
'''
1.先生成所有的砝码数的list
例如：示例一
生成amount=[1,2,1]
2.创建weight={0,}的集合，然后进行扩展
'''


import sys

n=int(input())
m=input().split()
x=input().split()
amount=[]
for i in range(n):
    for j in range(int(x[i])):
        amount.append(m[j])
weight={0,}
for i in amount:
    for j in list(weight):
        weight.add(int(i)+j)
print(len(weight))
