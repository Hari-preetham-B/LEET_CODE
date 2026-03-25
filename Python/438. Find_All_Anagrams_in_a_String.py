from collections import Counter
class Solution:
    def findAnagrams(self,s, p):
        p_count = Counter(p)
        window = Counter()
        
        res = []
        l = 0
        
        for r in range(len(s)):
            # add current character
            window[s[r]] += 1
            
            # shrink window if size > len(p)
            if r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            
            # check if equal
            if window == p_count:
                res.append(l)
        
        return res
