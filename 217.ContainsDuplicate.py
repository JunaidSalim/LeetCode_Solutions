class Solution(object):
    def containsDuplicate(self, nums):
        number_set  = set()
        for i in nums:
            if i in number_set:
                return True
            else:
                number_set.add(i)
        return False