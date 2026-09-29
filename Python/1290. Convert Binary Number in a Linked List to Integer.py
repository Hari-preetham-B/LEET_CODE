# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        c=0
        r=0
        t=l=head
        while t:
            c+=1
            t=t.next
        while l:
            if l.val==1:
                r+=2**(c-1)
                c-=1
                l=l.next
            else:
                c-=1
                l=l.next
        return r
        
