class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = 0
        for i in range(len(nums)):
            if i > ind:
                return False
            ind = max(ind, i + nums[i])
        return True

            
            