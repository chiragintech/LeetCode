class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums - length = n
        # ans - length = 2n
        # ans[i] = nums[i] and ans[i+n] == nums[i]
        # ans = 2 nums array concatenated
        # return ans
        nums.extend(nums)
        return nums