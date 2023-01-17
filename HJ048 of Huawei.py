'''
描述

输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。
链表的值不能重复。
构造过程，例如输入一行数据为:
6 2 1 2 3 2 5 1 4 5 7 2 2
则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2，剩下的2个一组表示第2个节点值后面插入第1个节点值，为以下表示:
1 2 表示为
2->1
链表为2->1

3 2表示为
2->3
链表为2->3->1

5 1表示为
1->5
链表为2->3->1->5

4 5表示为
5->4
链表为2->3->1->5->4

7 2表示为
2->7
链表为2->7->3->1->5->4

最后的链表的顺序为 2 7 3 1 5 4

最后一个参数为2，表示要删掉节点为2的值
删除 结点 2
则结果为 7 3 1 5 4
'''

示例1
输入：
5 2 3 2 4 3 5 2 1 4 3
输出：
2 5 4 1
说明：
形成的链表为2->5->3->4->1
删掉节点3，返回的就是2->5->4->1  

示例2
输入：
6 2 1 2 3 2 5 1 4 5 7 2 2
输出：
7 3 1 5 4

####solution（非链表构建）######

import sys

s=input().split()
n=int(s[0])
head=(s[1])
target=(s[-1])
l=[head,]
a=s[2::2]
b=s[3:-1:2]
for i in range(n-1):
    l.insert(l.index(b[i])+1,a[i])
l.remove(target)
print(' '.join(l))




