class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            minimum = min(nums)
            index = nums.index(minimum)
            nums[index] = nums[index] * multiplier 
        return nums
        
