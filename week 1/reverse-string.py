class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length_s = len(s)
        for i in range(length_s // 2): #integer division is for reversing only one time
            temp = s[i]
            s[i] = s[length_s - 1 - i]
            s[length_s - 1 - i] = temp
        