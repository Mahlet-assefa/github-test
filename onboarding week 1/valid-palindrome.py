class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"

        while i <= j:
            if s[i] not in letters:
                i += 1
            elif s[j] not in letters:
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                return False

        return True