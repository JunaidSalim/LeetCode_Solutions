class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i<n:
            value = nums[i] - 1
            check = value >=0 and value < n
            if check and nums[value]!=nums[i]:
                nums[value],nums[i] = nums[i],nums[value]
            else:
                i+=1
        result = []
        for i in range(n):
            if nums[i]!= i + 1:
                result.append(nums[i])
        return result