class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_score = 0
        zeros_count = 0
    
    # Count total number of ones
        ones_count = s.count('1')
    
    # Iterate through the string, excluding the last character
        for i in range(n - 1):
            if s[i] == '0':
                zeros_count += 1
            else:
                ones_count -= 1
            max_score = max(max_score, zeros_count + ones_count)
    
        return max_score

        