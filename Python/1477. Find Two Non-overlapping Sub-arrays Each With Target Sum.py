class Solution(object):
    def minSumOfLengths(self, nums, target):
        n = len(nums)
        INF = float('inf')
        minLen = [INF] * n

        best = INF
        left = 0
        windowSum = 0

        for right in range(n):
            windowSum += nums[right]

            while windowSum > target:
                windowSum -= nums[left]
                left += 1

            if windowSum == target:
                curLen = right - left + 1

                if left > 0 and minLen[left - 1] != INF:
                    best = min(best, minLen[left - 1] + curLen)

                if right > 0:
                    minLen[right] = min(minLen[right - 1], curLen)
                else:
                    minLen[right] = curLen
            else:
                if right > 0:
                    minLen[right] = minLen[right - 1]

        return best if best != INF else -1
