class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
             word_lower = word.lower() # to make the comparison case-insensetive
             if all(letter in "qwertyuiop" for letter in word_lower) or \
               all(letter in "asdfghjkl" for letter in word_lower) or \
               all(letter in "zxcvbnm" for letter in word_lower):
               #all function is used to make sure that all letters in the word exist
                result.append(word)
        return result