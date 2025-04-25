class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        count = n + 1
        l = 0
        s = 0
        for r in range(n):
            s+= nums[r]
            
            while s >= target:
                count = min(count,r-l+1)
                s -= nums[l]
                l +=1
            
        return count if count<=n else 0