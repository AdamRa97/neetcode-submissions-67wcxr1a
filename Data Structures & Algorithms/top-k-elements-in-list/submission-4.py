from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        arr = []

        for num, count in numCount.items():
            arr.append([count,num])
        arr.sort()
        
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res
