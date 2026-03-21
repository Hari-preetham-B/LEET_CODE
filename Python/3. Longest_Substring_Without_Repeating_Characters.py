class Solution(object):
    def lengthOfLongestSubstring(self, s):
        t=[]
        ml=0
        for i in s:
            while i in t:
                t.pop(0)
            t.append(i)
            ml=max(ml,len(t))
        return ml

  # or

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ml=0
        a=set()
        l=0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            else:
                a.add(s[r])
                ml=max(ml,r-l+1)
        return ml
        
