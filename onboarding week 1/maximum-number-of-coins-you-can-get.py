class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        my_pile=0
        bob=0
        me=len(piles)-2
        
        
        while bob < me:
           my_pile+=piles[me]
           bob+=1
           me-=2
        return my_pile


