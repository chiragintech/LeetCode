def helper(s,l,r):
    if l > r :
        return True
    if s[l] != s[r]:
        return False
    return helper(s,l+1,r-1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        print(s)
        return helper(s,0,len(s)-1)



