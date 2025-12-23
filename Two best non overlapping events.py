from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        min_heap = [] 
        max_value_so_far = 0
        answer = 0
        
        for start, end, value in events:
            while min_heap and min_heap[0][0] < start:
                _, val = heapq.heappop(min_heap)
                max_value_so_far = max(max_value_so_far, val)

            answer = max(answer, max_value_so_far + value)

            heapq.heappush(min_heap, (end, value))
        
        return answer
