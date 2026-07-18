class Solution(object):
    def minOperations(self, boxes):
        n=len(boxes)
        answer=[0]*n

        bc=0
        m=0
        for i in range(n):
            answer[i]+=m
            if boxes[i]=="1":
                bc+=1
            m+=bc
        
        bc=0
        m=0
        for i in range(n-1,-1,-1):
            answer[i]+=m
            if boxes[i]=="1":
                bc+=1
            m+=bc
        
        return answer
