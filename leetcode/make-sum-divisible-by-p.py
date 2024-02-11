class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0
        
        target_remainder = total_sum % p
        min_length = float('inf')
        current_remainder = 0
        seen_remainders = {0: -1}  # Initialize with dummy value to handle edge case
        
        for i, num in enumerate(nums):
            current_remainder = (current_remainder + num) % p
            complement_remainder = (current_remainder - target_remainder) % p
            if complement_remainder in seen_remainders:
                min_length = min(min_length, i - seen_remainders[complement_remainder])
            seen_remainders[current_remainder] = i
        
        return min_length if min_length < len(nums) else -1