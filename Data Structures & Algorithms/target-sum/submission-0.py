class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0
            if (i, currSum) in memo:
                return memo[i,currSum]

            add = dfs(i+1, currSum + nums[i])
            subtract = dfs(i+1, currSum - nums[i])
            res = add + subtract
            memo[i,currSum] = res
            return res
        return dfs(0,0)