class Solution(object):
    def fourSum(self, nums, target):
        result,n= [],len(nums)
        nums = sorted(nums)
        for i in range(n):
            for j in range(i+1,n):
                left,right = j+1,n-1
                while left<right:
                    sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if sum<target:
                        left+=1
                    elif sum>target:
                        right-=1
                    else:
                        toAppend = [nums[i],nums[j],nums[left],nums[right]]
                        if toAppend not in result:
                            result.append(toAppend)
                        left+=1
                        right-=1
        return result