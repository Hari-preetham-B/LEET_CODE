class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        curr_sum = 0
        min_len = float('inf')
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len
