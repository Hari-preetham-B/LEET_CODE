class Solution(object):
    def maxVowels(self, s, k):
        n=len(s)
        stri=s[:k]
        l=0
        c=0
        maxi=0
        for ch in stri:
            if ch in 'aeiou':
                c+=1
        maxi=c
        for r in range(k,n):
            if s[r] in 'aeiou':
                c+=1
            if s[l] in 'aeiou':
                c-=1
            if c>maxi:
                maxi=c
            l+=1
        return maxi
