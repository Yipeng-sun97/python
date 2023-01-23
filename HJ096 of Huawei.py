'''
描述
将一个字符串中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。
'''

示例1
输入：
Jkdi234klowe90a3

输出：
Jkdi*234*klowe*90*a*3*

####solution###
import sys

s=input()
res=[]

res.append(s[0])
for i in range(1,len(s)):
    if not res[-1].isdigit() and s[i].isdigit():
        res.append("*")
        res.append(s[i])
    elif res[-1].isdigit() and not s[i].isdigit():
        res.append("*")
        res.append(s[i])
    else:
        res.append(s[i])
if res[-1].isdigit():
    res.append('*')
if res[0].isdigit():
    res.insert(0,'*')
print(''.join(res)) 

#####solution####
给每个数字前后打上&（本想直接用*，但是样例有个*1**3*给挡住了），再把连续的&去掉，单独的&替换为*


s=input()
for i in '0123456789':
    s = s.replace(i,'&'+i+'&')
s = s.split('&&')
s = str(''.join(s)).replace('&','*')
print(s)

