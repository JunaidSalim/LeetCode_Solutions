class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxleft, maxright = 0, 0
        count = 0
        while left<=right:
            if height[left]<=height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    count += maxleft - height[left]  
                left+=1
            else:
                if height[right]>=maxright:
                    maxright = height[right]
                else:
                    count += maxright - height[right]    
                right-=1
        
        return count