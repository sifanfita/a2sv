class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numIndex = {num: i for i, num in enumerate(nums)}

        for operation in operations:
            idxReplace, newNum = operation
            idx = numIndex[idxReplace]
            nums[idx] = newNum
            del numIndex[idxReplace]
            numIndex[newNum] = idx

        return nums
      

            
        
        
        
        
    
    