'''
描述

有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。
下面是它的工作原理：
首先，选择一个单词作为密匙，如TRAILBLAZERS。
如果单词中包含有重复的字母，只保留第1个，将所得结果作为新字母表开头，并将新建立的字母表中未出现的字母按照正常字母表顺序加入新字母表。
如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y (实际需建立小写字母的字母表，此字母表仅为方便演示）
上面其他用字母表中剩余的字母填充完整。
在对信息进行加密时，信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。
因此，使用这个密匙， Attack AT DAWN (黎明时攻击)就会被加密为Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
'''
输入描述：
先输入key和要加密的字符串

输出描述：
返回加密后的字符串

示例1
输入：
nihao
ni
输出：
le

####solution###
word, s = input(), input()
letter = 'abcdefghijklmnopqrstuvwxyz ' # 注意末尾有个空格
midList = list(word+letter) # 前后拼接
key = list(set(midList)) # 用集合去重
key.sort(key = midList.index) # 恢复原有排序
dic = dict(zip(list(letter), key)) # 生成对照密码本
print(''.join([dic[i] for i in s])) # 输出结果
