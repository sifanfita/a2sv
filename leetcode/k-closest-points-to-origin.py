class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sorting the points based on their distance in ascending order
        sorted_points = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
        return sorted_points[:k]
        