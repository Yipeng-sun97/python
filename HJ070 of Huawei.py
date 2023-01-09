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

思路：
利用stack 栈 和指针来辅助完成。


import sys

while True:
    try:
        n=int(input())
        att=[]
        stack=[]
        res=0
        for i in range(n):
            s=list(map(int,input().split()))
            att.append(s)    #用构建的att存储矩阵的信息 att=[[50,10],[10,20],[20,5]]
        f=input()
        k=0
        for i in f:
            if i.isalpha():
                stack.append(att[k])  #利用stack 把 att压入栈中
                k+=1
            elif i==')' and len(stack)>=2:  #如果指针指向“）” 说明前两个矩阵需要计算
                a=stack.pop()
                b=stack.pop()
                res+=a[0]*a[1]*b[0]  #计算矩阵乘法的计算量
                stack.append([b[0],a[1]]) #生成新的矩阵信息放入栈中
        print(res)
    except:
        break
