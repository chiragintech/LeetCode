class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = sum(accounts[0][0:3])
        for i in range(len(accounts)):
                if ans < sum(accounts[i][0:len(accounts[i])]):
                    ans = sum(accounts[i][0:len(accounts[i])])
        return ans
                    