class Solution:
    def largestOddNumber(self, num: str) -> str:
        for index, n in reversed(list(enumerate(num))):
            if int(n) % 2==1:
                return num[:index + 1]
        return ""