""" 
HJ5 进制转换
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
数据范围：保证结果在 1 \le n \le 2^{31}-1 \1≤n≤2 
31
 −1 
注意本题有多组输入
输入描述：
输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据，请参考帖子https://www.nowcoder.com/discuss/276处理多组输入的问题。
输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。 
"""


########solution_1########   

print(int(input(),16)) #int(s,16) 可以直接转换

########solution_2########
 
str1 = input()
str2 = str1[2:]
n = len(str2)
dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
x1 = 0
for word in str2:
    if word in dic:
        x1 = x1 + dic[word]*16**(n-1)
        n = n - 1
    else:
        x1 = x1 + int(word)*16**(n-1)
        n = n - 1
print(x1)



    
