class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        
        while l <= r:
            mid = (l + r) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == -1:
                r = mid - 1
            else:
                l = mid + 1