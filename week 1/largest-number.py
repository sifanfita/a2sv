class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(self.compare))
        return "".join(nums).lstrip("0") or "0"

    def compare(self, x, y):
        xy = x + y
        yx = y + x
        return int(yx) - int(xy)
        