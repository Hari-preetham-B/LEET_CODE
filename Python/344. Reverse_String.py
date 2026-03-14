class Solution(object):
    def reverseString(self, s):
        s[:]=s[::-1]
# class Solution(object):
#     def reverseString(self, s):
#         i=0
#         n=len(s)
#         while(i<n//2):
#             temp=s[n-i-1]       // this way also possible but inefficient 
#             s[n-i-1]=s[i]
#             s[i]=temp
#             i+=1
#         return s
        
