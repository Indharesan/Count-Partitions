class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        squares = set(i * i for i in range(1, n + 1))

        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                c2 = a2 + (b * b)
                if c2 in squares:
                    c = int(c2 ** 0.5)
                    if c <= n:
                        count += 1
        return count            

                       
