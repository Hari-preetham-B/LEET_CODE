class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
        
# or

class Solution(object):
    def sortedSquares(self, nums):
        l=0
        r=len(nums)-1
        pos=r
        result=[0]*(pos+1)
        while l<=r:
            ls=nums[l]**2
            rs=nums[r]**2
            if ls<rs:
                result[pos]=rs
                r-=1
                pos-=1
            else:
                result[pos]=ls
                l+=1
                pos-=1
        return result
