class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        stri="abcdefghijklmnopqrstuvwxyz"
        res=[0]*(len(s)+1)
        ans=[]
        arr=[]
        final=""
        for i in range(len(s)):
            arr.append(stri.index(s[i]))
        for start,end,dir in shifts:
                if dir==1:
                    res[start]+=1
                    res[end+1]-=1
                else:
                    res[start]-=1
                    res[end+1]+=1
        summed=0
        pxsu=[]
        for j in range(len(res)-1):
            summed+=res[j]
            pxsu.append(summed)
        for k in range(len(pxsu)):
            pxsu[k]=pxsu[k]+arr[k]
        for l in pxsu:
            ans.append(stri[l%26])
        for letter in ans:
            final+=letter
        return final



































        # arr=[]
        # calc=[]
       
        # for k in range(len(shifts)):
        #     l=shifts[k][0]
        #     r=shifts[k][1]
        #     op=shifts[k][2]
        #     if r+1<len(res):
        #         if op==0:
        #             res[l]-=1
        #             res[r+1]+=1
        #             print(res)
        #         else:
        #             res[l]+=1
        #             res[r+1]-=1
        #     calc.append() 

                 

            

        
         
        