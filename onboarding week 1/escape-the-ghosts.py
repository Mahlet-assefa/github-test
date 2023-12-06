class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        isfound=True
        for x, y in ghosts:
            escape=abs(target[0])+abs(target[1])
            ghostroute=abs(x-target[0])+ abs(y-target[1])
            
            if ghostroute <= escape :
                return False
            
        return isfound


























            
           