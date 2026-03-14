class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge=""
        if len(word1)>=len(word2):
            j=0
            for i in range(len(word1)):
                
                if j<len(word2):
                    merge+=word1[i]+word2[j]
                else:
                    merge+=word1[i]
                j+=1
        else:
            j=0
            for i in range(len(word2)):
                if j<len(word1):
                    merge+=word1[i]+word2[i]
                else:
                    merge+=word2[i]
                j+=1
        return (merge)
        
