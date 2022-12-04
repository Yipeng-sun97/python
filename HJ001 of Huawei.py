'''
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。


输入：
hello nowcoder
输出：
8
说明：
最后一个单词为nowcoder，长度为8 

'''

##########solution##########


s = input()
print(len(s.strip().split()[1])) #print(len(s.strip().split(" ")[1]))


或者

s = input()
print(len(s.split()[-1])) #print(len(s.split(" ")[-1]))


#########函数说明############
s.strip() 的作用是删除s首尾的空值

Eg：

str = "00000003210Runoob01230000000"; 
print str.strip( '0' );  # 去除首尾字符 0

输出：
3210Runoob0123
 
 
str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();

输出：
Runoob
