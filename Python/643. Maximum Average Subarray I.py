class Solution(object):
    def findMaxAverage(self, nums, k):
        W_sum=sum(nums[:k])
        max_sum=W_sum
        for r in range(k,len(nums)):
            W_sum+=nums[r]
            W_sum-=nums[r-k]
            max_sum=max(max_sum,W_sum)
        return max_sum/float(k)
