class Solution(object):
    def isValid(self, s):
        t = []
        
        for i in s:
            if i in "([{":
                t.append(i)
            elif i == ')':
                if not t or t[-1] != '(':
                    return False
                t.pop()
            elif i == ']':
                if not t or t[-1] != '[':
                    return False
                t.pop()
            elif i == '}':
                if not t or t[-1] != '{':
                    return False
                t.pop()
            else:
                return False
        
        return len(t) == 0
