class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        r = m - 1 if m<=n else n - 1
        result = 1
        for i in range(1,r+1):
            result = result * ((N - r + i)/ i )
        return round(result)