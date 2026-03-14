# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l=0
        h=n
        while l<=h:
            mid=(l+h)//2
            r=guess(mid)
            if r==0:
                return mid
            elif r== -1:
                h=mid-1
            else :
                l=mid+1
