class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        nums[n-k%n:] =reversed(nums[n-k%n:])
        nums[:n-k%n]=reversed(nums[:n-k%n]) 
        nums.reverse()