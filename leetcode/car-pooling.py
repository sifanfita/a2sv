class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trip[2] for trip in trips) + 1
        prefix_sum = [0] * n
        for nums, froms, tos in trips:
            prefix_sum[froms] += nums
            prefix_sum[tos] -= nums  # No need to check tos+1, just tos itself
        current_capacity = 0
        for num in prefix_sum:
            current_capacity += num
            if current_capacity > capacity:
                return False
        return True
