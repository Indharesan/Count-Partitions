class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)

        mn = complexity[0]
        for i in range(1, n):
            if mn >= complexity[i]:
                return 0
            mn = min(mn, complexity[i])

 
        parent = list(range(n+1))
        def find(x):
            # path-compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def remove(x):
            
            parent[x] = x+1

        import heapq

        unlocked = [False]*n
        unlocked[0] = True

       
        heap = []
        i = 1
        while i < n:
            if complexity[i] > complexity[0]:
                heapq.heappush(heap, (complexity[i], i))
                remove(i)           
                i = find(i+1)
            else:
                i += 1

        ans = 1

    
        for step in range(1, n):
            if not heap:
                return 0
            ans = (ans * len(heap)) % MOD

            comp_u, u = heapq.heappop(heap)
            unlocked[u] = True
            v = find(u+1)
            while v < n:
                if complexity[v] > complexity[u]:
                    heapq.heappush(heap, (complexity[v], v))
                    remove(v)
                    v = find(v+1)
                else:
                    v = v + 1

        return ans
