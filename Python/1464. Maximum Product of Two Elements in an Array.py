class Solution(object):
    def maxProduct(self, nums):
        
        first_max = 0
        second_max = 0

        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num

        return (first_max - 1) * (second_max - 1)


#or
class Solution(object):
    def maxProduct(self, nums):
        
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first-1)*(second -1)
        
