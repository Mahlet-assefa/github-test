class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0  

        for index, w in enumerate(s):
            if j < len(spaces) and index == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(w)

        return ''.join(ans)