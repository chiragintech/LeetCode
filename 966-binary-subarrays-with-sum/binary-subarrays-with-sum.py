class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def solve(g):
            if g < 0:
                return 0
            l = 0
            s = 0
            count1 = 0
            for r in range(len(nums)):
                s += nums[r]
                while s > g:
                    s -= nums[l]
                    l += 1   
                count1 += (r-l+1)
            return count1

        return solve(goal) - solve(goal-1)

            
