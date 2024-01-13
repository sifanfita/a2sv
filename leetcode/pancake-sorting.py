class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        flips = []
        
        for target in range(len(arr), 0, -1):
            index = arr.index(target)
            arr[:index + 1] = arr[:index + 1][::-1]
            arr[:target] = arr[:target][::-1]
            flips.extend([index + 1, target])
        
        return flips      