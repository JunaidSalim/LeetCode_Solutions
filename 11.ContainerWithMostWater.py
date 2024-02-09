class Solution(object):
    def maxArea(self, height):
        right = len(height)-1
        left=0
        max_area=0
        while left<right:
            area = (right - left) * min(height[right],height[left])
            max_area = max(max_area,area)
            if height[left]<height[right]: left+=1
            else: right-=1
        return max_area

        return max
        