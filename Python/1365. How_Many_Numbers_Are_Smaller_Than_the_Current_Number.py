class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # Step 1: Count frequency of each number (0–100)
        count = [0] * 101
        
        for num in nums:
            count[num] += 1
        
        # Step 2: Convert to prefix sum array
        for i in range(1, 101):
            count[i] += count[i - 1]
        
        # Step 3: Build result
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])
        
        return result
        
