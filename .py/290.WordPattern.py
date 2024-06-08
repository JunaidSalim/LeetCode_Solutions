class Solution(object):
    def wordPattern(self, pattern, s):
        str = s.split()
        if len(str)!=len(pattern):
            return False
        return map(str.index,str)==map(pattern.find,pattern)
        