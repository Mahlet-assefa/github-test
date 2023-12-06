class Solution:
    def largestGoodInteger(self, num: str) -> str:
       maxval = '' 
       result=[]
       for i in range(2, len(num)): 
        if num[i] == num[i - 1] == num[i - 2]: 
            result.append(num[i - 2:i + 1] ) 
        else: 
            result.append('')
       maxval=max(result)
       return maxval
        
            
        

