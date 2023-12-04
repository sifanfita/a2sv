class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        for i in range(min(len(word1),len(word2))):
            merged+=word1[i]
            merged+=word2[i]
        if len(word1)>len(word2):
            k=len(word1)-len(word2)
            for i in range(len(word1)-k, len(word1)):
                merged+=word1[i]
        elif len(word2)>len(word1):
            k=len(word2)-len(word1)
            for i in range(len(word2)-k, len(word2)):
                merged+=word2[i]
        return merged
        
        