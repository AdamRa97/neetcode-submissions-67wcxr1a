class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtrack(start, remain, current):
            if remain == 0:
                res.append(current.copy())
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                current.append(candidates[i])
                backtrack(i+1, remain - candidates[i], current)
                current.pop()
        backtrack(0,target, subset)
        return res