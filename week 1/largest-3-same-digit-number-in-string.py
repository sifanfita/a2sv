class Solution:
    def largestGoodInteger(self, num: str) -> str:
         max_good_integer = ""
         for i in range(len(num) - 2):
             current_substring = num[i:i+3]
             unique_digit = current_substring[0]
             if current_substring == unique_digit * 3:
                  max_good_integer = max(max_good_integer, current_substring)
         return max_good_integer
           
        
        
    
        