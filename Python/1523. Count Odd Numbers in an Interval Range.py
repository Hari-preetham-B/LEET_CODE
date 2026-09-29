class Solution(object):
    def countOdds(self, low, high):
        return (high+1)//2-low//2

# or

class Solution(object):
    def countOdds(self, low, high):
        c=0
        for i in range(low,high+1):
          if i%2 !=0:
            c+=1
        return c
