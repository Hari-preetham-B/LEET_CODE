class Solution(object):
    def searchRange(self, nums, target):
        i=nums.count(target)
        if i==0:
            return [-1,-1]
        if i==1:
            j=nums.index(target)
            return [j,j]
        if i>1:
            j=nums.index(target)
            return [j,j+i-1]
