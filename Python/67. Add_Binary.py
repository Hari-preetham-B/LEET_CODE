class Solution(object):
    def addBinary(self, a, b):
        i=int(a,2)
        j=int(b,2)
        n=i+j
        s=bin(n)
        return s[2:]
