class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        counts = 0
        for element, count in counter.items():
            if count % (element + 1) == 0:
                counts += count
            else:
                counts += (count // (element + 1) + 1) * (element + 1)
        return counts


        