class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Data Structure Use: HashMap used for storing Num : Frequency
        # Go through nums array once by updating/adding in the frequency KV pairs
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        if len(nums) <= 0:
            return False
        if max(freqMap.values()) > 1:
            return True
        return False
