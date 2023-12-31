class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        evenSum = sum(x for x in nums if x % 2 == 0)

        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            result.append(evenSum)

        return result
        