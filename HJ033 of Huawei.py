'''
描述

原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
'''
示例1

输入：
10.0.3.193
167969729

输出：
167773121
10.3.3.193

#######solution#######
def ip_to_int(s):
    s = list(map(int, s.split('.')))
    s = [bin(i)[2:] for i in s]
    s = ''.join([(8-len(i)) * '0' + str(i) for i in s])
    print(int(s,2))

def int_to_ip(s):
    s = bin(int(s))[2:]
    s = (32 - len(s)) * '0' + s
    s = [str(int((s[i:i+8]), 2)) for i in range(0,len(s),8)]
    print('.'.join(s))

while True:
    try:
        s = input()
        if '.' in s:
            ip_to_int(s)
        else:
            int_to_ip(s)
    except:
        break
