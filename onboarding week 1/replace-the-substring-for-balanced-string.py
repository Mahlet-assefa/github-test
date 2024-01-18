class Solution:
    def balancedString(self, s: str) -> int:
        ans = len(s)
        my_dict = collections.Counter(s)
        r = 0

        for l, c in enumerate(s):
            my_dict[c] -= 1
            while r < len(s) and all(my_dict[c] <= len(s) // 4 for c in 'QWER'):
                ans = min(ans, l - r + 1)
                my_dict[s[r]] += 1
                r += 1

        return ans