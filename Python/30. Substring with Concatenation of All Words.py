class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        wordLen = len(words[0])
        numWords = len(words)
        totalLen = wordLen * numWords
        n = len(s)
        if n < totalLen:
            return []
        need = {}
        for w in words:
            need[w] = need.get(w, 0) + 1
        result = []
        for offset in range(wordLen):
            left = offset
            count = 0
            window = {}
            right = offset
            while right + wordLen <= n:
                word = s[right:right + wordLen]
                if word not in need:
                    window = {}
                    count = 0
                    left = right + wordLen
                else:
                    window[word] = window.get(word, 0) + 1
                    count += 1
                    while window[word] > need[word]:
                        leftWord = s[left:left + wordLen]
                        window[leftWord] -= 1
                        count -= 1
                        left += wordLen
                    if count == numWords:
                        result.append(left)
                        leftWord = s[left:left + wordLen]
                        window[leftWord] -= 1
                        count -= 1
                        left += wordLen
                right += wordLen
        return result
