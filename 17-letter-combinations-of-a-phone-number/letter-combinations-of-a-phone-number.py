store = {2: ["a","b","c"],3 : ["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
def helper(p,up):
    if up == p:
        return []
    if len(up) == 0:
        return [p]
    num = int(up[0])
    l = []
    for i in range(len(store[num])):
        l.extend(helper(p + store[num][i],up[1:]))
    return l
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = helper("", digits)
        return l