from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_index = 0
        for i, num in enumerate(flips):
            max_index = max(max_index, num)
            if max_index == i + 1:
                count += 1
        return count