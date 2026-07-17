class Solution(object):
    def pivotArray(self, nums, p):
        sl=[]
        bl=[]
        c=[]
        for i in nums:
            if i<p:
                sl.append(i)
            elif i>p:
                bl.append(i)           #using 3 lists
            else:
                c.append(i)
        num=sl+c+bl
        return num

# or

class Solution(object):
    def pivotArray(self, nums, p):
        n = len(nums)
        less_count = sum(1 for num in nums if num < pivot)
        equal_count = sum(1 for num in nums if num == pivot)

        result = [0] * n
        i, j, k = 0, less_count, less_count + equal_count              #using single result list

        for num in nums:
            if num < pivot:
                result[i] = num
                i += 1
            elif num == pivot:
                result[j] = num
                j += 1
            else:
                result[k] = num
                k += 1

        return result
        
