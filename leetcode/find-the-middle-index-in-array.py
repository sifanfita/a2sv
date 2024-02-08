from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        
        # Calculate prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        # Find potential middle indices
        for i in range(n):
            left_sum = prefix_sum[i] - nums[i]  # Sum of elements to the left of index i
            right_sum = prefix_sum[-1] - prefix_sum[i]  # Sum of elements to the right of index i
            if left_sum == right_sum:
                return i
        
        # If no middle index found
        return -1