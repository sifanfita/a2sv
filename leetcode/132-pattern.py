class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  
        ak = float('-inf')  

        for num in reversed(nums):
          
            if num < ak:
                return True
            while stack and stack[-1] < num:
                ak = stack.pop()
            stack.append(num)  

        return False
