class Solution(object):
    def longestConsecutive(self, nums):
        nums=list(set(nums))
        nums.sort()
        longest=1
        current=1
        for i in range (1,len(nums)):
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                longest=max(longest,current)
                current=1
        return max(longest,current) if nums else 0
