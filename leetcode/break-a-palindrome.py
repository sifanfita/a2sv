class Solution:
  def breakPalindrome(self, palindrome: str) -> str:
    if len(palindrome) == 1:
      return ''

    palindrome_list = list(palindrome)

    for i in range(len(palindrome) // 2):
      if palindrome_list[i] != 'a':
        palindrome_list[i] = 'a'
        return ''.join(palindrome_list)

    palindrome_list[-1] = 'b'
    return ''.join(palindrome_list)