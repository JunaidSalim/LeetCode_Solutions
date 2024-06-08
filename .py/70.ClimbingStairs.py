class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        prev, curr = 1, 2
        for i in range(n - 2):
            next_step = prev + curr
            prev, curr = curr, next_step
        return curr
