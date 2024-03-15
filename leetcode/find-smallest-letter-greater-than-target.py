

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter_to_number = {chr(ord('a') + i): i + 1 for i in range(26)}
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letter_to_number[letters[mid]] <= letter_to_number[target]:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l % len(letters)]