class Solution:
  def maxScoreIndices(self, nums: List[int]) -> List[int]:
    zeros = nums.count(0)
    ones = len(nums) - zeros
    ans = [0]  # the division at index 0
    leftZeros = 0
    leftOnes = 0
    max_score = ones  # `leftZeros` + `rightOnes`

    for i, num in enumerate(nums):
      leftZeros += num == 0
      leftOnes += num == 1
      rightOnes = ones - leftOnes
      score = leftZeros + rightOnes
      if max_score == score:
        ans.append(i + 1)
      elif max_score < score:
        max_score = score
        ans = [i + 1]

    return ans