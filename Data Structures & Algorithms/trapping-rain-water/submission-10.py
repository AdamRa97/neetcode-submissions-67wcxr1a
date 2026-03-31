class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1
        area = 0

        while l <= r:
            if height[l] <= height[r]:
                maxL = max(maxL, height[l])
                area += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                area += maxR - height[r]
                r -= 1
        return area