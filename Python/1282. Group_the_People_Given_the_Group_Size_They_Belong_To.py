class Solution(object):
    def groupThePeople(self, g):
        grp={}
        r=[]
        for i,size in enumerate(g):
            if size not in grp:
                grp[size]=[]
            grp[size].append(i)
            if len(grp[size])==size:
                r.append(grp[size])
                grp[size]=[]
        return r
        
