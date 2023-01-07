'''
描述

输入整型数组和排序标识，对其元素按照升序或降序进行排序
 
输入描述：

第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序
'''

示例1

输入：
8
1 2 4 9 3 55 64 25
0

输出：
1 2 3 4 9 25 55 64


####solution######
import sys


def sort_num(s, c):
    s = s.split()
    s = [int(i) for i in s]
    if c == "0":
        s.sort()
    elif c == "1":
        s.sort(reverse=True)
    s = [str(i) for i in s]
    print(" ".join(s))


while True:
    try:
        n = input()
        s = input()
        c = input()
        sort_num(s, c)
    except:
        break
