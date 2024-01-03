class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array in increasing order
        n = len(nums)
        count = 0

        left = 0
        right = n - 1

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
        