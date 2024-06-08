class Solution(object):
    def lengthOfLastWord(self, s):
        length = len(s)
        count=0
        check = 0
        for i in range(length):
            if s[length-i-1]==" ":
                if check==1:
                    return count
            else:
                check=1
                count = count + 1

        return count