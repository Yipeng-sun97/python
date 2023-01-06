'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格
输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5

解题思路
主要考虑这个数字能被除1与self本身整除的情况,将所有除数顺序输出,最后再排序,打印时候用空格分隔
个人感觉,这里用while循环比较好,for循环不太好实现.
'''


先从2开始
在从3开始
能整除的都是质因子
#######solution########
x=int(input())
y=2
z=[]
while x!=y:
    if x%y==0:
        x=x/y
        z.append(str(y)) #输出格式的限制需要转换成str
    else:
        y+=1
z.append(str(int(x))) #循环之后剩下的一定是质数
print(' '.join(z)) #.join需要str格式时使用

#or#
n = int(input())
res = list()

for i in range(2, n + 1):
    while n % i == 0:
        n = n // i
        res.append(str(i))

    if n == 1:
        break

    if i > pow(n, 0.5):
        res.append(str(n))
        break

print(" ".join(res))

