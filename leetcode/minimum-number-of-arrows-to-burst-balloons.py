class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
        
        points.sort(key=lambda x: x[1])  # Sort by end points

        arrows = 1
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] > end:  
                arrows += 1  
                end = points[i][1]  
        return arrows
        