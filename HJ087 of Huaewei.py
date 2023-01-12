'''
描述

密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符

二、字母:
0 分: 没有字母
10 分: 密码里的字母全都是小（大）写字母
20 分: 密码里的字母符合”大小写混合“

三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字

四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号

五、奖励（只能选符合最多的那一种奖励）:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号

最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱（Very_Weak）
'''

示例1

输入：
38$@NoNoN

输出：
VERY_SECURE

说明：
样例的密码长度大于等于8个字符，得25分；大小写字母都有所以得20分；
有两个数字，所以得20分；包含大于1符号，所以得25分；
由于该密码包含大小写字母、数字和符号，所以奖励部分得5分，
经统计得该密码的密码强度为25+20+20+25+5=95分。

#####solution####
import sys

def score_func(s):
    res=[0,0,0,0]
    score=0
    n=len(s)
    #判断长度
    if n<=4:
        score+=5
    elif n>=8:
        score+=25
    else:
        score+=10
    #分类判断
    d=[]
    a=[]
    o=[]
    for i in s:
        if i.isdigit():
            d.append(i)
            res[0]=1
        elif i.isalpha():
            a.append(i)
            res[1]=1
        else:
            o.append(i)
            res[2]=1
    #判断数字
    if len(d)==1:
        score+=10
    elif len(d)>1:
        score+=20
    #判断符号
    if len(o)==1:
        score+=10
    elif len(o)>1:
        score+=25
    #判断字母
    a1=[0,0]
    for i in a:
        if i.isupper():
            a1[0]=1
        elif i.islower():
            a1[1]=1
    if sum(a1)==1:
        score+=10
    elif sum(a1)==2:
        score+=20
        res[3]=1
    #reward
    if sum(res)==4:
        score+=5
    else:
        if res[0]+res[1]+res[2]==3:
            score+=3
        else:
            if res[0]+res[1]==2:
                score+=2
    #rank

    if score>=90:
        print('VERY_SECURE')
    elif score>=80:
        print('SECURE')
    elif score>=70:
        print('VERY_STRONG')
    elif score>=60:
        print('STRONG')
    elif score>=50:
        print('AVERAGE')
    elif score>=25:
        print('WEAK')
    else:
        print('VERY_WEAK')

while True:
    try:
        s=input()
        score_func(s)
    except:
        break
