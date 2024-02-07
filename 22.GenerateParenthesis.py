class Solution(object):
    def generateParenthesis(self, n):
        def Generate(left,right,res):
            if len(res)==n*2:
                result.append(res)
                return
            if left<n:
                Generate(left+1,right,res+"(")
            if right<left:
                Generate(left,right+1,res+")")
        
        result = []
        Generate(0,0,"")
        return result