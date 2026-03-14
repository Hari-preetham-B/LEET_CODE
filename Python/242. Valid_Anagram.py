class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        a = set(s)
        for i in a:
            if s.count(i) != t.count(i):
                return False
        return True
# you can also do this
# return sorted(s) == sorted(t) 
