class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n==0 or n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        left,right= 1,n-2
        while left<=right:
            mid = (left)+((right-left)//2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return mid
        