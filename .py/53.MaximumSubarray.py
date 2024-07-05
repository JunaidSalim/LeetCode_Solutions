class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -(2**31)
        temp = 0
        for i in range(n):
            temp += nums[i]
            if temp>max_sum:
                max_sum = temp
            if temp<0:
                temp = 0
        return max_sum 