class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l=0
        r=0
        n=len(name)
        m=len(typed)
        if m<n:
            return False
        while r<m:
            
            if l<n and name[l] == typed[r]:
                l+=1
                r+=1
            else:
                if r!=0 and name[l-1] == typed[r]:            
                    r+=1
                else:
                    return False 
        return l==n


       
