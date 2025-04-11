class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if (int(math.log10(nums[i])) + 1) % 2 == 0:
                res +=1
        return res
