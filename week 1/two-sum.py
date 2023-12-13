
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        n = len(nums)
        
        for i in range(n):
            j = target - nums[i]
            if j in num_dict:
                return [num_dict[j], i]
            num_dict[nums[i]] = i
        
        return [] 


        