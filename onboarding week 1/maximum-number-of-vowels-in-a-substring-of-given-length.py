class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        my_vow={'a','e','i','o','u'}
        l=0
        count=0
        res=0
        for i in range(len(s)):
            if s[i] in my_vow:
                count+=1
            else:
                count+=0
            if i-l+1>k:
                if s[l] in my_vow:
                    count-=1
                else:
                    count+=0
                l+=1          
            res=max(res,count)
        return res


