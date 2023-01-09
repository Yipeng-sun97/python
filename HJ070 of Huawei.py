'''
描述

矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。
编写程序计算不同的计算顺序需要进行的乘法次数。
'''
示例1

输入：
3
50 10
10 20
20 5
(A(BC))

输出：
3500


#######solution#####
import sys

while True:
    try:
        n=int(input())
        att=[]
        stack=[]
        res=0
        for i in range(n):
            s=list(map(int,input().split()))
            att.append(s)
        f=input()
        k=0
        for i in f:
            if i.isalpha():
                stack.append(att[k])
                k+=1
            elif i==')' and len(stack)>=2:
                a=stack.pop()
                b=stack.pop()
                res+=a[0]*a[1]*b[0]
                stack.append([b[0],a[1]])
        print(res)
    except:
        break
