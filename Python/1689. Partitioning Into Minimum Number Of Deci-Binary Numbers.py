class Solution(object):
    def minPartitions(self, n):
        m=0
        for i in n:
            d=int(i)
            if d>m:
                m=d
        return m


# or

class Solution(object):
    def minPartitions(self, n):
        for i in range(9, 0, -1):
            if str(i) in n:
                return int(i)
        
