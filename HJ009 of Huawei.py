'''
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围： 1 \le n \le 10^{8} \1≤n≤10 
8
  
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入：
9876673
复制
输出：
37689
'''
#####solution######
s = list(input()[::-1]) # 数字左右翻转，再转化为列表
s_set = list(set(s)) # 用集合去重，再变成列表
s_set.sort(key = s.index) # 集合会改变顺序，要恢复原有顺序
print(''.join(s_set))


######solution#####

m = input()
m = m[::-1]
n = ''
for i in m:
    if i not in n:
        n += i
print(n)
