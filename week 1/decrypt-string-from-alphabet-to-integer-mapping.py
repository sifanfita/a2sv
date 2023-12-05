class Solution:
    def freqAlphabets(self, s: str) -> str:
      result = []
      i = len(s) - 1

      while i >= 0:
        if s[i] == '#':
            mapped_char = int(s[i - 2:i])
            result.append(chr(ord('a') + mapped_char - 1))
            i -= 3
        else:
            result.append(chr(ord('a') + int(s[i]) - 1))
            i -= 1

      return ''.join(result[::-1])
  