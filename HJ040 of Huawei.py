描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000 

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数


#####solution######
s = input()
res=[0,0,0,0]

for i in s:
    if i.isalpha():   #是否为字母
        res[0]+=1
    elif i==' ':
        res[1]+=1
    elif i.isnumeric():    #是否为数字
        res[2]+=1
    else:
        res[3]+=1

for i in res:
    print(i)

    
######solution######

import re #利用正则

s=input()
res=[0,0,0,0]

res[0] = len(re.findall(r"[a-zA-Z]", s)) #字母
res[1] = len(re.findall(r"[\s]", s))    #空格字符
res[2] = len(re.findall(r"[0-9]", s))   #数字
res[3] = len(s) - sum(res[0:3])    #剩下的其他
 
for i in res:
    print(i)
