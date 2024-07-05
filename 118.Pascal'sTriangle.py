class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        result = [[1]]
        for i in range(numRows-1):
            temp = []
            temp.append(result[-1][0])
            for j in range(1,len(result[-1])):
                temp.append(result[-1][j-1]+result[-1][j])
            temp.append(result[-1][-1])
            result.append(temp)
        return result