from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        max_heap = [ (-ord(c), count) for c, count in  counts.items()]
        heapify(max_heap)
        ans = []

        while max_heap:
            neg_char, count = heappop(max_heap)
            char = chr(-neg_char)
            use = min(count, repeatLimit)
            ans.append(char * use)

            if count > use :
                if not max_heap:
                    break
                next_neg_char, next_count = heappop(max_heap)
                next_char = chr(-next_neg_char)
                ans.append(next_char)
                if next_count > 1:
                    heappush(max_heap, (next_neg_char, next_count - 1))
                heappush(max_heap, (neg_char, count - use))
        
        return "".join(ans)
