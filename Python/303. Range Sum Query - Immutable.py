class NumArray(object):
    def __init__(self, nums):
        self.num=nums
        self.n=len(nums)
        self.prefix=[0]*self.n
        self.prefix[0]=self.num[0]
        for i in range(1,self.n):
            self.prefix[i]=self.prefix[i-1]+self.num[i]
    def sumRange(self, left, right):
        if left==0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
