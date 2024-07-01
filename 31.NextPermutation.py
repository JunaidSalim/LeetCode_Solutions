class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index = -1
        
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        
        if index == -1:
            nums.reverse()
            return
       
        smallest_index = index + 1
        for i in range(index + 1, n):
            if nums[i] > nums[index] and nums[i] <= nums[smallest_index]:
                smallest_index = i
        
        nums[index], nums[smallest_index] = nums[smallest_index], nums[index]
        nums[index + 1:] = reversed(nums[index + 1:])
