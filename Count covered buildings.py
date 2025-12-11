from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)

        for x, y in buildings:
            row[x].append(y)
            col[y].append(x)

        for x in row:
            row[x].sort()
        for y in col:
            col[y].sort()

        covered = 0

        for x, y in buildings:
            ys = row[x]
            xs = col[y]

            import bisect
            yi = bisect.bisect_left(ys, y)

            xi = bisect.bisect_left(xs, x)

            if yi > 0 and yi < len(ys) - 1 and xi > 0 and xi < len(xs) - 1:
                covered += 1

        return covered
