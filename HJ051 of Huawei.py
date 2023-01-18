描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表结点定义如下：
struct ListNode
{
    int m_nKey;
    ListNode* m_pNext;
};
正常返回倒数第k个结点指针，异常返回空指针.
要求：
(1)正序构建链表;
(2)构建后要忘记链表长度。


'''
输入描述：
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值

输出描述：
输出一个整数

示例1
输入：
8
1 2 3 4 5 6 7 8
4

输出：
5
'''

####利用链表###########
import sys

# 需要自己自己构建链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def func(l,s,k):
    head=ListNode()
    while k>0:
        head.next=ListNode(s.pop()) #利用栈倒序输出
        head=head.next
        k-=1
    print(head.val)

while True:
    try:
        l = int(input())
        s = list(map(int, input().split()))
        k = int(input())
        func(l,s,k)
    except:
        break



####solution####非链表方法####
import sys

def func(s,target):
    print(s[-target])

while True:
    try:
        n=input()
        s=input().split()
        target=int(input())
        func(s,target)
    except:
        break






