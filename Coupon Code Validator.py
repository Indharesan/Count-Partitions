from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        valid_business = set(order)

        buckets = {b: [] for b in order}

        pattern = re.compile(r'^[A-Za-z0-9_]+$')

        for c, b, active in zip(code, businessLine, isActive):
            if (
                active and
                b in valid_business and
                c and
                pattern.match(c)
            ):
                buckets[b].append(c)

        result = []
        for b in order:
            result.extend(sorted(buckets[b]))

        return result
