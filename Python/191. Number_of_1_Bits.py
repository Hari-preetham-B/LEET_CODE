class Solution(object):
    def hammingWeight(self, n):
        c=0
        s=bin(n)[2:]
        for i in s:
            if i=='1':
                c+=1
        return c
        
