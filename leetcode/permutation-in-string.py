from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter_s1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == counter_s1:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            if window[s2[i - len(s1)]] == 1:
                del window[s2[i - len(s1)]]
            else:
                window[s2[i - len(s1)]] -= 1

            if window == counter_s1:
                return True

        return False
        