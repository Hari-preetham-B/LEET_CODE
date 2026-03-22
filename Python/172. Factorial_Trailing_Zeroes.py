class Solution(object):
    def trailingZeroes(self, n):
        if n<=4:
            return 0
        sum=0
        while n>1:
            sum+=n//5
            n=n//5
        return sum
        
