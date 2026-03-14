class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m:
                result.append(True)
            else:
                result.append(False)
        return result
        
