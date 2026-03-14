class Solution(object):
    def removeElement(self, nums, val):
        c=0
        for i in nums:
            if i ==val:
                c+=1
        for i in range(c):
            nums.remove(val)
        n=len(nums)
        for i in range(c):
            nums.append(51)
        return n
