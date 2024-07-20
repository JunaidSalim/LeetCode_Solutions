class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = -1
        
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        
        if index == -1:
            nums.reverse()
            return nums
       
        smallest_index = index + 1
        for i in range(index + 1, n):
            if nums[i] > nums[index] and nums[i] <= nums[smallest_index]:
                smallest_index = i
        
        nums[index], nums[smallest_index] = nums[smallest_index], nums[index]
        nums[index + 1:] = reversed(nums[index + 1:])
        return nums

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = nums.copy()
        result.append(prev.copy())
        n = factorial(len(nums))
        for i in range(n-1):
            next_perm = self.nextPermutation(prev.copy())
            if next_perm not in result:
                result.append(next_perm.copy())
            prev = next_perm
        return result