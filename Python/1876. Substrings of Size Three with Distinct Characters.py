class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        for i in range(2,len(s)):
            if len({s[i],s[i-1],s[i-2]})==3:
                count+=1
        return count
