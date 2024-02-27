class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(s: int, path: List[int]) -> None:
      ans.append(path)

      for i in range(s, len(nums)):
        backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return ans