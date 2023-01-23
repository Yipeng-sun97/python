##solution 1 ####

构建一个二维数组


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1 for j in range(i + 1)] for i in range(rowIndex + 1)] #构建二位数组
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[-1]
      
      
 ####soluton2#####

一维数组滚动计算

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r=[1]
        for i in range(1,rowIndex+1):
            r.insert(0,0)
            for j in range(i):
                r[j]=r[j]+r[j+1]
        return r
        
            

                

        
