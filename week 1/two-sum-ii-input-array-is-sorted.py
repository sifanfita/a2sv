class Solution:
   def twoSum(self, nums, target):
       left = 0
       right = len(nums) - 1
       cur_sum = 0
       while nums[left] + nums[right] != target:
          cur_sum = nums[left] + nums[right]
          if cur_sum < target:
              left += 1
          else:
              right -= 1
       return [left + 1, right + 1]
  