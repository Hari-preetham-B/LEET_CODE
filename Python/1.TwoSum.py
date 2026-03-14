class Solution(object):
    def twoSum(self, nums, target):
        l={}
        for i in range(len(nums)):
            l[nums[i]]=i
        for i in range(len(nums)):
            d=target-nums[i]
            if d in l and l[d]!=i:
                r=[i,l[d]]
                return r
