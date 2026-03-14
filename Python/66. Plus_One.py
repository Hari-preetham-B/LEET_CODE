class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s+=str(i)
        n=int(s)
        n=n+1
        s=str(n)
        l=[]
        for i in s:         
            l.append(int(i))
        return l
