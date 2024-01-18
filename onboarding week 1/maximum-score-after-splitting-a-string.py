class Solution:
    def maxScore(self, s: str) -> int:
        total=[0]*len(s)
        ans=0
        prefix=0
        cnt=0
        
        for j in range(len(s)):
            prefix+=int(s[j])
            total[j]+=prefix
        idx=total[-1]
        for i in range(len(total)-1):
            if s[i]=="0":
                cnt+=1
            else:
               idx-=1
            ans=max(ans,idx+cnt)
        return ans
        

        
        

