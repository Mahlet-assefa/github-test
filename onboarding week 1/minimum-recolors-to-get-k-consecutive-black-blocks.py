class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sliced=blocks[:k]
        cnt=sliced.count('W')
        ans=sliced.count('W')
        #print(ans)
        for r in range(k,len(blocks)):
            cnt += blocks[r] == 'W'
            cnt -= blocks[r - k] == 'W'
            ans = min(ans, cnt)
        return ans