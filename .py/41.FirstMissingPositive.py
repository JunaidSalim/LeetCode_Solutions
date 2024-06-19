class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            value = nums[i] - 1

            check = value >= 0 and value < n

            if check and nums[i]!=nums[value]:
                nums[i],nums[value] = nums[value],nums[i]
            else:
                i+=1

        for i in range(n):
            if nums[i]!=i + 1:
                return i + 1

        return n+1