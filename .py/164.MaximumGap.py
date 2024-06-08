class Solution(object):
    def maximumGap(self, nums):
        nums = sorted(nums)
        n = len(nums)
        max_gap = 0
        for i in range(n-1):
            max_gap = max(nums[i+1]-nums[i],max_gap)
        return max_gap