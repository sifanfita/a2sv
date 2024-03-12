class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n 
        while l <= r:
            mid = (l + r) // 2  # Calculate mid correctly to avoid overflow
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
