class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        mp={0:1}
        p=0
        for i in range(len(nums)):
            p+=nums[i]
            if p-k in mp:
                count+=mp[p-k]
            mp[p]=mp.get(p,0)+1
        return count
        
