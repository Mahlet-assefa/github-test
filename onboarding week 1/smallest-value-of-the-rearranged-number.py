class Solution:
    def smallestNumber(self, num: int) -> int:
        neg=num<0
        num=abs(num)
        if num==0:
            return 0
        cnt=[0]*10
        while num:
            num, rem = divmod(num, 10)
            cnt[rem]+=1
            res=""
        if neg:
            for i in range(9,-1,-1):
                if cnt[i]:
                    res+= str(i) * cnt[i]
            return -(int(res))
        if cnt[0]:
            for i in range(1,10):
                if cnt[i]:
                    res+=str(i)
                    cnt[i] -= 1
                    break
        for i in range(10):
            if cnt[i]:
                res += str(i) * cnt[i]
        return int(res)
            
            
