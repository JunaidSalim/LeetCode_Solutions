class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1]* n

        for i in range(1,n):
            left_product[i] = nums[i-1] * left_product[i-1]

        for i in range(n-2,-1,-1):
            right_product[i] = nums[i+1] * right_product[i+1]

        product = [left_product[i] * right_product[i] for i in range(n)]
        return product
        