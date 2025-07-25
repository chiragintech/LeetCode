def helper(p, up, target):
    if sum(p) == target:
        return [p]
    if up == [] or sum(p) > target:
        return []
    res = []
    num = up[0]
    res.extend(helper([num] + p, up[:], target))
    res.extend(helper(p, up[1:], target))
    return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        up = candidates
        return helper([], up, target)