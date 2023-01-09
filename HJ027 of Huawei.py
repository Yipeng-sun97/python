'''
描述

定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。
'''
输入描述：
输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k

输出描述：
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。


示例1
输入：
3 abc bca cab abc 1
输出：
2
bca


示例2
输入：
6 cab ad abcd cba abc bca abc 1

输出：
3
bca
说明：
abc的兄弟单词有cab cba bca，所以输出3,经字典序排列后，变为bca cab cba，所以第1个字典序兄弟单词为bca   



#######solution########
import sys

def func(s,t,k):
    c=0
    res=[]
    dic={}
    for i in t:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
    for i in s:
        if i==t:
            continue
        h={}
        for x in i:
            if x in h:
                h[x]+=1
            else:
                h[x]=1
        if h==dic:
            res.append(i)
            c+=1
    res.sort()
    print(c)
    print(res[k-1])

while True:
    try:
        all=input().split()
        n=int(all[0])
        s=all[1:n+1]
        k=int(all[-1])
        t=all[-2]
        
        func(s,t,k)
    except:
        break        
