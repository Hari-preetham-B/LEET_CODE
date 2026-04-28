class Solution(object):
    def isHappy(self, n):
        def next(x):
            return sum(int(d)**2 for d in str(x))
        s=n
        f=next(n)
        while f!=1 and s!=f:
            s=next(s)
            f=next(next(f))
        return f==1
