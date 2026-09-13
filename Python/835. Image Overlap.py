class Solution(object):
    def largestOverlap(self, img1, img2):
        n=len(img1)
        a=[]
        b=[]
        for r in range(n):
            for c in range(n):
                if img1[r][c]==1:
                    a.append((r,c))
                if img2[r][c]==1:
                    b.append((r,c))
        if not a or not b:
            return 0
        count={}
        best=0
        for (x1,y1) in a:
            for (x2,y2) in b:
                v=(x2-x1,y2-y1)
                if v in count:
                    count[v]+=1
                else:
                    count[v]=1
                if count[v]>best:
                    best=count[v]
        return best
