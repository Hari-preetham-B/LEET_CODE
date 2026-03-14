class Solution(object):
    def isPerfectSquare(self, num):
        n=int(num**.5)
        if num==n**2:
            return True
        else:
            return False

        
