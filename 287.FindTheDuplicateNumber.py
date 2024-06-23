class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            value = nums[i] - 1

            check = value >= 0 and value < n

            if check and nums[i]!=nums[value]:
                nums[i],nums[value] = nums[value],nums[i]
            else:
                i+=1
        return nums[n-1]