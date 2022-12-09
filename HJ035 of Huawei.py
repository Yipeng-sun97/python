
蛇形矩阵

描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：

1 3 6 10 15

2 5 9 14

4 8 13

7 12

11



########solution##########

首先得算第一排：（n+1）*（n+2）//2
下一排就是上一排去掉第一个元素
然后之后的都-1

n=int(input())
res=[]

for i in range(n):
    if i==0:
        for e in range(n):
            res.append((e+1)*(e+2)//2)
    elif i!=0:
        res=[e-1 for e in res[1:]]
        
    print(' '.join(map(str,res))) #res中是int 改成str才能用.join()
