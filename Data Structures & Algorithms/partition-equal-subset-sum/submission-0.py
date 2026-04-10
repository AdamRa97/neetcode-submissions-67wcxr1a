class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        capacity = sum(nums) // 2
        memo = {}

        def dfs(i, capacity):
            if capacity == 0:
                return True
            if i >= len(nums) or capacity < 0:
                return False
            
            if (i, capacity) in memo:
                return memo[i,capacity]
            
            take = dfs(i+1, capacity - nums[i])
            skip = dfs(i+1, capacity)
            res = take or skip
            memo[i,capacity] = res
            return res
        return dfs(0,capacity)