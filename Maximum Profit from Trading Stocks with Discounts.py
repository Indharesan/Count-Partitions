from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:

        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        NEG = -10**15

        def merge(a, b):
            res = [NEG] * (budget + 1)
            for i in range(budget + 1):
                if a[i] == NEG:
                    continue
                for j in range(budget - i + 1):
                    if b[j] != NEG:
                        res[i + j] = max(res[i + j], a[i] + b[j])
            return res

        def dfs(u: int):
          
            dp0 = [NEG] * (budget + 1)
            dp1 = [NEG] * (budget + 1)

            dp0[0] = 0
            dp1[0] = 0

            child_dp = [dfs(v) for v in children[u]]

            base = [NEG] * (budget + 1)
            base[0] = 0
            for c0, _ in child_dp:
                base = merge(base, c0)

            dp0 = base[:]
            dp1 = base[:]

            full_cost = present[u]
            full_profit = future[u] - full_cost
            if full_cost <= budget:
                temp = [NEG] * (budget + 1)
                temp[full_cost] = full_profit
                for _, c1 in child_dp:
                    temp = merge(temp, c1)
                for i in range(budget + 1):
                    dp0[i] = max(dp0[i], temp[i])

            disc_cost = present[u] // 2
            disc_profit = future[u] - disc_cost
            if disc_cost <= budget:
                temp = [NEG] * (budget + 1)
                temp[disc_cost] = disc_profit
                for _, c1 in child_dp:
                    temp = merge(temp, c1)
                for i in range(budget + 1):
                    dp1[i] = max(dp1[i], temp[i])

            return dp0, dp1

        dp0_root, _ = dfs(0)
        return max(dp0_root)
