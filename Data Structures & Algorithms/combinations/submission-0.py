class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start, current):
            if len(current) == k:
                res.append(current.copy())
                return
            if len(current) > k:
                return
            
            for i in range(start, n+1):
                current.append(i)
                backtrack(i+1, current)
                current.pop()
        backtrack(1,subset)
        return res