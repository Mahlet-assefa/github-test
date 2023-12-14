class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = Counter()
        for a, b in matches:
            if a not in count:
                count[a] = 0
            count[b] += 1
        ans = [[], []]

        for w, l in count.items():
            if l < 2:
                ans[l].append(w)
        
        ans[0].sort()
        ans[1].sort()
        return ans
        
             