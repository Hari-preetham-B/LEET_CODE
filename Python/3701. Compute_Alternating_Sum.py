class Solution(object):
    def alternatingSum(self, nums):
        n=len(nums)
        a=nums[::2]
        b=nums[1::2]
        a=sum(a)
        b=sum(b)
        return a-b        
