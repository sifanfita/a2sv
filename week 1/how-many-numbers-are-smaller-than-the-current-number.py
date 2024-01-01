class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    Max = 100
    count = collections.Counter(nums)

    for i in range(1, Max + 1):
      count[i] += count[i - 1]

    return [0 if num == 0 else count[num - 1]
            for num in nums]