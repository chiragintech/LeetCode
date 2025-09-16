class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s) - 1
        l1 = list(s)
        vowels = set('AEIOUaeiou')
        while l < r and l < len(s) and r < len(s):
            if l1[l] in vowels and l1[r] in vowels:
                l1[l],l1[r] = l1[r],l1[l]
                l += 1
                r -= 1
            elif l1[l] in vowels:
                r -= 1
            elif l1[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(l1)
