from typing import List
from collections import defaultdict

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers  

        grouped = defaultdict(list)
        for e in events:
            etype, ts_str, arg = e
            ts = int(ts_str)
            grouped[ts].append((etype, arg))

        for ts in sorted(grouped.keys()):
            for u in range(numberOfUsers):
                if offline_until[u] != 0 and offline_until[u] <= ts:
                    offline_until[u] = 0

            for etype, arg in grouped[ts]:
                if etype == "OFFLINE":
                    uid = int(arg)
                    offline_until[uid] = ts + 60

            for etype, arg in grouped[ts]:
                if etype != "MESSAGE":
                    continue
                msg = arg.strip()
                if msg == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif msg == "HERE":
                    for u in range(numberOfUsers):
                        if offline_until[u] == 0:
                            mentions[u] += 1
                else:
                    tokens = msg.split()
                    for t in tokens:
                        if t.startswith("id"):
                            uid = int(t[2:])
                            mentions[uid] += 1

        return mentions
