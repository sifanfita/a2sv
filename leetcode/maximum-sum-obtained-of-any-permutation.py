class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0 ] * (len(nums)+1)
        for l,r in requests:
            prefix_sum[l] += 1
            prefix_sum[r+1] -= 1
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1] 
        prefix_sum = sorted(prefix_sum[:-1], reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for i in range(len(prefix_sum)):
            ans += nums[i] * prefix_sum[i]
            if prefix_sum[i] == 0:
                break
        return ans % (10**9 + 7)