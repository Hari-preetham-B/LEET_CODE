class Solution(object):
    def maxDepth(self, s):
        c=0
        m=0
        for i in s:
            if i=="(":
                c+=1
            m=max(c,m)
            if i==")":
                c-=1
        return m
