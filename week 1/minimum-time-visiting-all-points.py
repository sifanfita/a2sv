class Solution:
    import math
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            time_horizontal = abs(x2 - x1)
            time_vertical = abs(y2 - y1)
            time_diagonal = max(time_horizontal, time_vertical)

            
            total_time += time_diagonal
        return total_time
    
      
             
        
        
        
    
    
   
        
        
        
   
        