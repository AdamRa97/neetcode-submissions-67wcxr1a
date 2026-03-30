class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, a in enumerate(nums):
            if a > 0:
                break
            if idx > 0 and a == nums[idx-1]:
                continue
            l, r = idx+1, len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum == 0:
                    res.append((a,nums[l],nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1
        return res