class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = float('inf')
        min_difference = float('inf')
        n = len(nums)
        
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                difference = abs(res - target)
                
                if difference < min_difference:
                    min_difference = difference
                    result = res
                
                if res > target:
                    right -= 1
                elif res < target:
                    left += 1
                else:
                    return res  # res == target
        
        return result