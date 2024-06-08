class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = len(nums)
        product = 1
        for i in range(n):
            if nums[i]==0:
                return 0
            elif nums[i]<0:
                product *= -1

        return product
        