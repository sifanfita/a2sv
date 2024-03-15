class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid == x:
                return mid
            
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the loop exits without finding the exact square root,
        # return the floor value of the last considered number
        return right