'''
描述
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。

如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。

如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。


如，输入： By?e 输出： Be?y


输入描述：
输入字符串
输出描述：
输出字符串
'''
示例1
输入：
A Famous Saying: Much Ado About Nothing (2012/8).

输出：
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
  
  
 ######solution######
while True:
    try:
        s = input()
        a = ""
        for i in s:
            if i.isalpha():
                a += i
        b = sorted(a, key=str.upper) ##key = str.upper#可以忽略大小字母排序，而且相同的大小写字母按着顺序排序
        index = 0 #指针
        d = ""
        for i in range(len(s)):
            if s[i].isalpha():
                d += b[index]
                index += 1
            else:
                d += s[i]
        print(d)
    except:
        break
