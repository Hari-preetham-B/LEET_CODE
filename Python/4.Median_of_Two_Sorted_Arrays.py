class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l=sorted(nums1+nums2)
        n=len(l)
        if n%2==0:
            h=(l[n//2]+l[n//2-1])/2.0
            return h
        else:
            h= l[(n-1)//2]
            return h
