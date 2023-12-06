class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        maxCandy = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
        
        

