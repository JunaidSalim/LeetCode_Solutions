class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        hashmap = Counter(nums)
        for x in hashmap:
            if hashmap[x]==1:
                result.append(x)
        return result
        