class Solution(object):
    def longestCommonPrefix(self, strs):
       if not strs:
            return ""
        
       length = len(strs[0])
       result = ""
        
       for i in range(length):
            c = strs[0][i]
            check = True

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    check = False
                    break

            if check:
                result += c
            else:
                break

       return result
        