class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            n=nums+[target]
            n.sort()
            return(n.index(target))
        else:
            return(nums.index(target))
