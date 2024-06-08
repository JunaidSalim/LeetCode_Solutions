class Solution(object):
    def singleNumber(self, nums):
        hashmap = Counter(nums)
        for x in hashmap:
            if hashmap[x]==1:
                return x
        