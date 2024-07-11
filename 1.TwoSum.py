class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            more_needed = target - num
            if more_needed in map:
                return [map[more_needed], i]
            map[num] = i
        return [-1, -1]