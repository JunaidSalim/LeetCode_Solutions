class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n==0: return 0
        if n==1: return 1
        result = []
        for i in range(n):
            temp = []
            for j in range(i,n):
                if s[j] not in temp:
                    temp.append(s[j])
                else:
                    break
            if len(temp)>len(result):
                result = []
                result = temp
        return len(result)