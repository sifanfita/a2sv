class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges, key=lambda x: x[1], reverse=True)

        for num in range(left, right + 1):
            covered = False
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break
            if not covered:
                return False

        return True