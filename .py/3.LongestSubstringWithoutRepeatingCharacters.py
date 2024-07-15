class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left,right=0,0
        mpp=[-1] * 256
        count= 0
        while right<n:
            if mpp[ord(s[right])] != -1:
                left = max(left,mpp[ord(s[right])]+1)
            mpp[ord(s[right])] = right
            count = max(count,right-left+1)
            right+=1
        return count