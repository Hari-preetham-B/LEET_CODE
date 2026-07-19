class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, value):
        self.stack.append(value)
        if self.min_stack:
            current_min=min(value,self.min_stack[-1])
        else:
            current_min=value
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
