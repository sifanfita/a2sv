class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()

        ans = 0
        i = 0  # heaters' index (currently used)
        if houses == heaters:
            return 0

        for house in houses:
            while i + 1 < len(heaters) and abs(house - heaters[i]) > abs(heaters[i + 1] - house):
                i += 1  # The next heater is better.
            ans = max(ans, abs(heaters[i] - house))

        return ans
