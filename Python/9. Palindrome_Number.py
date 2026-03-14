class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if x==x[::-1]:
            l= True
        else:
            l= False
        return l
