class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        my_dict={}
        maxi=0
        res=0
        for i in range(len(answerKey)):
            my_dict[answerKey[i]] = my_dict.get(answerKey[i], 0) + 1
            #print(my_dict)
            maxi = max(maxi, my_dict[answerKey[i]])
            print(maxi)
            if res-maxi >= k:
                my_dict[answerKey[i-res]]-=1 
            else:
                res+=1
        return res
        
       
           