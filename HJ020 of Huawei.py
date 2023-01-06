'''
描述

密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

输入描述：

一组字符串。
输出描述：

如果符合要求输出：OK，否则输出NG
'''

输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出：

OK
NG
NG
OK

######solution#######

def check(pw):
    if len(pw) <= 8:			# 判断密码的长度
        return False
    
    checks = [0,0,0,0]			# 四种情况满足三种的辅助列表
    for c in pw:
        if c.isupper():			# 大写字母
            checks[0] = 1
        elif c.islower():		# 小写字母
            checks[1] = 1
        elif c.isdigit():		# 数字
            checks[2] = 1
        else:					# 其他字符
            checks[3] = 1
    if sum(checks) < 3:
        return False
        
    dc = {}
    for i in range(len(pw) - 2):		# 遍历所有的子字符串起点
        if pw[i:i+3] in dc:				# 在字典中搜索
            return False
        else:							# 如果未曾经出现过则加入字典中，等待之后的判定
            dc[pw[i:i+3]] = 1
    
    return True



while True:
    try:
        pw = input()
        if check(pw):
            print('OK')
        else:
            print('NG')
    except:
        break

