

""" 
HJ4 字符串分隔
描述
•连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
（注：本题有多组输入）
输入描述：
连续输入字符串(输入多次,每个字符串长度小于等于100)
输出描述：
依次输出所有分割后的长度为8的新字符串
示例1
输入：
abc
123456789
复制
输出：
abc00000
12345678
90000000 
"""


solution_1:
  
while True:
    try:
        str = input().strip()
        for i in range(0, len(str), 8):  #i 输出的0，8，16，32....
           print("{0:0<8}".format(str[i:i+8])). #{0:0<8}意思是小于8位长度后面用0补齐
    except:
        break
        
solution_2:
  
s=input()
l=len(s)
while len(s)>8:
    print(s[:8])
    s=s[8:]
s=s+'0'*(8-len(s))
print(s)
