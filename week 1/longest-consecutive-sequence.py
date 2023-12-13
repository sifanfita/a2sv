class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        numSet = set(nums)
        longestSequence = 0

        for num in numSet:
            if num - 1 not in numSet:
                currentNum = num
                currentSequence = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentSequence += 1

                longestSequence = max(longestSequence, currentSequence)

        return longestSequence
        