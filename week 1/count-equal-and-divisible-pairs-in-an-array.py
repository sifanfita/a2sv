from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counts = 0 #initialize counts
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    counts += 1

        return counts