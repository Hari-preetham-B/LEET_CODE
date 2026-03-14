class Solution(object):
    def categorizeBox(self, l, w, h, m):
        v=l*w*h
        if((l>=10000 or w>=10000 or h>=10000 or v>=10**9) and m>=100):
            return "Both"
        elif (l>=10000 or w>=10000 or h>=10000 or v>=10**9):
            return "Bulky"
        elif (m>=100):
            return "Heavy"
        else:
            return "Neither"
        
