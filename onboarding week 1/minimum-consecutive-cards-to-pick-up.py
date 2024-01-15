class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        result = float("inf")
        for i, x in enumerate(cards):
            if x in seen:
                result = min(result, i-seen[x]+1)
            seen[x] = i
        if result != float("inf") :
            return result 
        else:
             return -1
        
