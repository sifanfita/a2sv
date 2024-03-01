class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, cur, sums):
            if sums == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sums > target:
                return
            cur.append(candidates[i])
            backtrack(i, cur, sums + candidates[i])
            cur.pop()
            backtrack(i+1, cur, sums)    
        backtrack(0, [], 0)
        return res       