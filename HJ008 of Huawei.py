'''
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开
输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4
复制
输出：
0 3
1 2
3 4
复制
示例2
输入：
3
0 1
0 2
8 9
复制
输出：
0 3
8 9

'''

##########solution##########
  
dic={}
n = int(input())#输入的第一个数字n 表示有n行
for i in range(n):
    str_input = input()
    s = int(str_input.split()[0])
    a = int(str_input.split()[-1])
    dic[s]=dic.get(s,0)+a
for key in sorted(dic):
    print(key,dic[key]) 
    
 ###########solution#######
dic = dict()
n = int(input())
for i in range(n):
    key, value = map(int, input().split())
    dic[key] = dic.get(key, 0) + value # 利用好get(key, default value)函数

for key in sorted(dic):
    print(key, dic[key])
  

