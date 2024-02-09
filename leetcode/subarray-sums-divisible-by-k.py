class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}  # Dictionary to store prefix sum and its count
        total_sum = 0
        count = 0
        
        for num in nums:
            total_sum += num
            desired_sum = total_sum % k
            count += prefix_sum.get(desired_sum, 0)
            prefix_sum[desired_sum] = prefix_sum.get(desired_sum, 0) + 1
        
        return count