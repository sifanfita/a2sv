class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        len_arr = len(arr)
        if len_arr < 3:
            return False
        i = 1
        while i < len_arr and arr[i - 1] < arr[i]: #moving up the mountain
            i += 1
        if i == 1 or i == len_arr:
            return False
        while i < len_arr and arr[i - 1] > arr[i]: #move down the mountain
            i += 1
        return i == len_arr
        
        