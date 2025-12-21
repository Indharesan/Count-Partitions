from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        sorted_pair = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            need_delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    need_delete = True
                    break
            
            if need_delete:
                deletions += 1
                continue

            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

            if all(sorted_pair):
                break
        
        return deletions
