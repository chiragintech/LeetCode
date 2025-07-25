def helper(word, changed,k):
    if len(word) > k:
        return word[k-1]
    for i in range(len(word)):
        changed += chr(ord(word[i]) + 1)
    print(word + changed)
    return helper(word + changed, "", k)
    
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        changed = ""
        return helper(word,changed,k)