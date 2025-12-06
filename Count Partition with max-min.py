class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1

        max_dq, min_dq = collections.deque(), collections.deque()
        left = 0
        window_sum = 0

        for right in range(n):
            
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                window_sum = (window_sum - dp[left]) % mod
                left += 1

                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()    

            window_sum = (window_sum + dp[right]) % mod
            dp[right + 1] = window_sum
        
        return dp[n] % mod        
