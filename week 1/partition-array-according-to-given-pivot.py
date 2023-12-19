class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_elements = []
        greater_elements = []
        equal_elements = []
        n = len(nums)
        for i in range(n):
            if nums[i] < pivot:
                less_elements.append(nums[i])
            elif nums[i] == pivot:
                equal_elements.append(nums[i])

            else:
                greater_elements.append(nums[i])
            
        
        nums = less_elements + equal_elements + greater_elements
        return nums