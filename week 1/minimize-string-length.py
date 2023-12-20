class Solution:
  def minimizedStringLength(self, s: str) -> int:
      unique_characters = {*s} # {*s} unpack string character to unique individual element
      return len(unique_characters) 