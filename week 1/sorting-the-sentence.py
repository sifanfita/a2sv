class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_indices = [(word[:-1], int(word[-1])) for word in words]
        sorted_words = [word for word, _ in sorted(word_indices, key=lambda x: x[1])]
        return ' '.join(sorted_words)
        