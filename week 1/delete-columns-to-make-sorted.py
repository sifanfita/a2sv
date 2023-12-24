class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    no_col_deleted = 0

    for j in range(len(strs[0])):
      for i in range(len(strs) - 1):
        if strs[i][j] > strs[i + 1][j]:
          no_col_deleted += 1
          break

    return no_col_deleted