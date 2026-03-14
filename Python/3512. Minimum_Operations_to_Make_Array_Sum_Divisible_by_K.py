class Solution(object):
    def minOperations(self, nums, k):
        a=sum(nums)
        return a%k
        
