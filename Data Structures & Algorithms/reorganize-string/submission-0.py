import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-i,char] for char,i in count.items()]
        heapq.heapify(heap)
        res = ""
        prev = None
        while heap:
            count, char = heapq.heappop(heap)
            res += char
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            count += 1
            if count < 0:
                prev = [count, char]
        
        return res if len(res) == len(s) else ""