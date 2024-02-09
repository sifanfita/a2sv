from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = {0: 1}  # Stores the frequency of prefix sums
        
        current_sum = 0
        for num in nums:
            current_sum += num
            # Check if there exists a prefix sum such that current_sum - prefix_sum == goal
            count += prefix_sum.get(current_sum - goal, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
