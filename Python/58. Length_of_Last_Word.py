class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split()
        n=len(a)
        return len(a[n-1])
