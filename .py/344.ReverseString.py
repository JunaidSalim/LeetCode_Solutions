class Solution(object):
    def reverseString(self, s):
        length = len(s)
        j = length - 1
        for i in range(length/2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j-=1
        return s
