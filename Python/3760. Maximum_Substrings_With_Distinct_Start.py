class Solution(object):
    def maxDistinct(self, s):
        a=""
        count=0
        for i in s:
            if i not in a:
                a+=i
                count+=1
        return count

or 

class Solution(object):
    def maxDistinct(self,s):
        return len(set(s))
