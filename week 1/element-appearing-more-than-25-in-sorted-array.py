class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        limit = n // 4
        
        count = 1
        first_num = arr[0]
        
        for i in range(1, n):
            if arr[i] == first_num:
                count += 1
                if count > limit:
                    return first_num
            else:
                count = 1
                first_num = arr[i]
        
        return first_num
          
        