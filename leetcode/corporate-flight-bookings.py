class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n + 1)  # Increase prefix_sum size by 1
        for start, end, seats in bookings:
            prefix_sum[start-1] += seats
            prefix_sum[end] -= seats

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i-1]

        return prefix_sum[:-1]  # Remove the last element as it's not needed
