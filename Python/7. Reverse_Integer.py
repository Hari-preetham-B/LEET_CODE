class Solution(object):
    def reverse(self, x):
        if x<0:
            x=x*(-1)
            r=int((str(x))[::-1])
            if (r<-2**31) or r>(2**31-1):
                return 0
            return -1*r
        else:
            r=int((str(x))[::-1])
            if (r<-2**31) or r>(2**31-1):
                return 0
            return r
        
