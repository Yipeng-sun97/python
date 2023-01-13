'''
最长回文子串
'''

返回其长度

####solution#####

s=input()
mx=0
for i in range(len(s)):
  for j in range(len(s),i,-1):
    if s[i:j]==s[i:j][::-1]:
      mx=max(mx,j-i)
print(mx)
      

