from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        length = 0

        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1
            ans += length

        return ans
