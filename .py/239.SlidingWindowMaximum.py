from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n*k==0:
            return []

        deq = deque()
        maxArr = []
        for i in range(n):
            if deq and deq[0]<i-k+1:
                deq.popleft()


            while deq and nums[deq[-1]]<nums[i]:
                deq.pop()


            deq.append(i)

            if i>=k-1:
                maxArr.append(nums[deq[0]])

        return maxArr