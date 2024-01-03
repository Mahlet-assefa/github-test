class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        pro=0
        while i<j:
            if skill[0]+skill[-1]!=skill[i]+skill[j]:
                return -1
            pro+=skill[i]*skill[j]
            i+=1
            j-=1
        return pro
            