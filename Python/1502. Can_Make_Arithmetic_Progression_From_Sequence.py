class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i]!=arr[i+2]-arr[i+1]:
                return False
        return True
        
