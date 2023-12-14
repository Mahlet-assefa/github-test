class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        my_set=set()
        result = float("inf")
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                my_set.add(fronts[i])
        return min([num for num in fronts + backs
                if num not in my_set] or [0])
       
                        
                
                    

        
                        
        

        
            