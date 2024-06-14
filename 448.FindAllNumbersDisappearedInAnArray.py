class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        result = []
        while(i<n):
            value = nums[i] - 1
            check = value >= 0 and value < n
            if check and nums[value]!=nums[i]:
                nums[value],nums[i] = nums[i],nums[value]
            else:
                i += 1
        for i in range(n):
            if nums[i]!=i+1:
                result.append(i+1)

        return result