'''
描述

对输入的字符串进行加解密，并输出。
加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
解密方法为加密的逆过程。

 
输入描述：

第一行输入一串要加密的密码
第二行输入一串加过密的密码
输出描述：

第一行输出加密后的字符
第二行输出解密后的字符
'''
示例1

输入：
abcdefg
BCDEFGH

输出：
BCDEFGH
abcdefg

####solution#######
import sys

def code(s):
    c=[]
    for i in s:
        if i.isalpha():
            if i.islower():
                if i=='z':
                    i='A'
                else:
                    i=chr(ord(i)-31)
            elif i.isupper():
                if i=='Z':
                    i='a'
                else:
                    i=chr(ord(i)+33)
        if i.isdigit():
            if i=='9':
                i='0'
            else:
                i=str(int(i)+1)
        c.append(i)
    print(''.join(c))

def decode(s):
    c=[]
    for i in s:
        if i.isalpha():
            if i.islower():
                if i=='a':
                    i='Z'
                else:
                    i=chr(ord(i)-33)
            elif i.isupper():
                if i=='A':
                    i='z'
                else:
                    i=chr(ord(i)+31)
        if i.isdigit():
            if i=='0':
                i='9'
            else:
                i=str(int(i)-1)
        c.append(i)
    print(''.join(c))

s=list(input())
code(s)
s=list(input())
decode(s)
