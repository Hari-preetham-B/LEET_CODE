class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1] ,reverse=True)
        total=0
        for count,units in boxTypes:
            take=min(count,truckSize)
            total+=take*units
            truckSize-=take
            if truckSize==0:
                break
        return total
        
