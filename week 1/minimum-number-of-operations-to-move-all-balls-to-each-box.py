class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        total_distance = 0
        balls_to_left = 0
        for i in range(n):
            result[i] += total_distance
            balls_to_left += int(boxes[i])
            total_distance += balls_to_left

   
        total_distance = 0
        balls_to_right = 0
        for i in range(n - 1, -1, -1):
            result[i] += total_distance
            balls_to_right += int(boxes[i])
            total_distance += balls_to_right

        return result

    
        
        