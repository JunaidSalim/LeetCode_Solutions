class Solution(object):
    def minimumTotal(self, triangle):
        temp = triangle[-1]
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                temp[j]= min(temp[j],temp[j+1]) + triangle[i][j]
        return temp[0]