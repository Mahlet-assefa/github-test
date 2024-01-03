class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        res=[]
        summed=0
        while l<r:
            summed=numbers[l]+numbers[r]
            if summed==target: 
                res.append(l+1)
                res.append(r+1)
                return res
            elif summed<target:
                l+=1
            else:
                r-=1
        





        