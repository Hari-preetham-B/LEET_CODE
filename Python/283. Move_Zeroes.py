class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
# class Solution(object):
#     def moveZeroes(self, nums):
#         n=len(nums)                  //     this can also be done in this way
#         t=[0]*n
#         j=0
#         for i in nums:
#             if i!=0:
#                 t[j]=i
#                 j+=1
#         for i in range(n):
#             nums[i]=t[i]
    
        
