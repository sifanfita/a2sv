class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        pairs = 0
        for num in count:
            pairs += min(count[num], count[k - num])
        return pairs // 2