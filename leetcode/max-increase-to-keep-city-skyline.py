class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])  
        colMax = [0] * num_cols 
        
        for j in range(num_cols):
            for i in range(num_rows):
                colMax[j] = max(colMax[j], grid[i][j])
        rowMax = list(map(max, grid))
        max_increase = sum(min(i, j) for i in rowMax for j in colMax)
        return max_increase - sum(map(sum, grid))
           
        
        

       
