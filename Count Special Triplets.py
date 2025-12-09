class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        from collections import Counter
        
        right = Counter(nums)
        left = Counter()
        
        ans = 0
        
        for j in range(len(nums)):
            right[nums[j]] -= 1  
            
            value = nums[j]
            target = value * 2
            
            ans = (ans + left[target] * right[target]) % MOD
            
            left[value] += 1      
        
        return ans
        
