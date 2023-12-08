class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive_numbers = [x for x in nums if x > 0]
        negative_numbers = [x for x in nums if x < 0]

        result = []

        for i in range(n // 2):
            result.append(positive_numbers[i])
            result.append(negative_numbers[i])  
        return result