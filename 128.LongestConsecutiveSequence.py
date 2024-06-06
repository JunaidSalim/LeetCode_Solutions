class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        longest = 0
        for num in l:
            if num - 1 not in l:
                current = 1
                while num + 1 in l:
                    current +=1
                    num+=1
                longest = max(current,longest)

        return longest
        