class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for word in words:
          lowerWord = set(word.lower())
          for row in rows:
            if lowerWord.issubset(row):
              ans.append(word)
        return ans