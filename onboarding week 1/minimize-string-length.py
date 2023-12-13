class Solution:
    def minimizedStringLength(self, s: str) -> int:
        my_set = set()
        my_set.update(s)
        return len(my_set)
