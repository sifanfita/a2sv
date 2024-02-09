class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = {0: 1}  # Dictionary to store prefix sum and its count
        total_sum = 0
        counts = 0
        
        for num in nums:
            total_sum += num
            # If prefix_sum[total_sum - k] exists, it means there's a subarray with sum k
            counts += prefix_sum.get(total_sum - k, 0)
            prefix_sum[total_sum] = prefix_sum.get(total_sum, 0) + 1
        
        return counts
