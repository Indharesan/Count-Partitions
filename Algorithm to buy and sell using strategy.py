from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2

        orig = sum(strategy[i] * prices[i] for i in range(n))

        deltaA = [-strategy[i] * prices[i] for i in range(n)]
        deltaB = [(1 - strategy[i]) * prices[i] for i in range(n)]

        prefA = [0] * (n + 1)
        prefB = [0] * (n + 1)

        for i in range(n):
            prefA[i + 1] = prefA[i] + deltaA[i]
            prefB[i + 1] = prefB[i] + deltaB[i]

        best = 0

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            gain = (prefA[mid] - prefA[l]) + (prefB[r] - prefB[mid])
            best = max(best, gain)

        return orig + best
