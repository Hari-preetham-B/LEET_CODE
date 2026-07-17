class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        r=[0]*n
        p,n=0,1
        for i in nums:
            if i>0:
                r[p]=i
                p+=2
            else:
                r[n]=i
                n+=2
        return r
        
