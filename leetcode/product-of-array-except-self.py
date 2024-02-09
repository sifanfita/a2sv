class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * n  # All elements will be 0
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        prefix_sum = [0] * n
        if zero_count == 1:
            for i in range(n):
                prefix_sum[i] = product if nums[i] == 0 else 0
        else:
            for i in range(n):
                prefix_sum[i] = product // nums[i]
        return prefix_sum
