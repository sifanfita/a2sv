class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstMin = float('inf')
        secondMin = float('inf')

        for num in nums:
            if num <= firstMin:
                firstMin = num
            elif num <= secondMin:
                secondMin = num
            else:
                return True

        return False
            
        