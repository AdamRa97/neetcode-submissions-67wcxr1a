class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(current):
            if len(current) == len(nums):
                res.append(current.copy())
                return
            elif len(current) > len(nums):
                return
            
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack(current)
                current.pop()
        backtrack(subset)
        return res