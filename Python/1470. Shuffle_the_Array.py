class Solution(object):
    def shuffle(self, nums, n):
        c=[]
        for i in range (n):
            c.append(nums[i])
            c.append(nums[n+i])
        return c
        
