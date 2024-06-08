class Solution(object):
    def hammingWeight(self, n):
       bit_count = 0
       while n > 0:
           n &=(n-1)
           bit_count+=1
       return bit_count