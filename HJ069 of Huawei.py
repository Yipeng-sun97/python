'''
矩阵乘法
输入描述：

第一行包含一个正整数x，代表第一个矩阵的行数
第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数
第三行包含一个正整数z，代表第二个矩阵的列数
之后x行，每行y个整数，代表第一个矩阵的值
之后y行，每行z个整数，代表第二个矩阵的值

输出描述：

对于每组输入数据，输出x行，每行z个整数，代表两个矩阵相乘的结果
'''
输入：
2
3
2
1 2 3
3 2 1
1 2
2 1
3 3

输出：
14 13
10 11

说明：
1 2 3
3 2 1 
乘以
1 2
2 1
3 3
等于
14 13
10 11  

######solution####
import sys

x = int(input())
y = int(input())
z = int(input())
a1 = [list(map(int, input().split())) for i in range(x)]
a2 = [list(map(int, input().split())) for i in range(y)]
result = [[0] * z for i in range(x)]
for i in range(x):
    for j in range(z):
        for k in range(y):
            result[i][j] += int(a1[i][k]) * int(a2[k][j])
    
    print(*result[i])


