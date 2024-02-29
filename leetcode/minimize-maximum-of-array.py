class Solution:
  def minimizeArrayValue(self, nums: List[int]) -> int:
    ans = 0
    prefix = 0

    for i, num in enumerate(nums):
      prefix += num
      prefix_average = math.ceil(prefix / (i + 1))
      ans = max(ans, prefix_average)

    return ans