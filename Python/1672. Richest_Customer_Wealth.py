class Solution(object):
    def maximumWealth(self, accounts):
        c=[]
        for i in accounts:
            c.append(sum(i))
        h=max(c)
        return h
   
