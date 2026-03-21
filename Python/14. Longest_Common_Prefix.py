class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre = strs[0]
        n=len(strs)
        for i in range(1,n):
            while strs[i].find(pre) != 0:
                pre = pre[:-1]
                if pre == "":
                    return ""
        
        return pre
