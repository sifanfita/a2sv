class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)

        for i in range(0, n, 2 * k):
            segment = s[i:i + k]
            reversed_segment = segment[::-1]
            result.append(reversed_segment + s[i + k:i + 2 * k])

        return ''.join(result)
        