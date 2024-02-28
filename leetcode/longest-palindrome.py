from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        odd_count = 0
        my_dict = defaultdict(int)
        for char in s:
            my_dict[char] += 1
        for count in my_dict.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1
                odd_count = 1

        return result + odd_count
       

       

       