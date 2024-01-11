class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        start_index = len(piles) // 3
        # Select every second element starting from the start_index until the end of the list
        selected_piles = sorted_piles[start_index::2]
        return sum(selected_piles)
