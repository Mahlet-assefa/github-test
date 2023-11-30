class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=1
        if not strs:
            return ""
        minlength=min(len(str)for str in strs)
        for i in range(minlength):
            x=strs[0][i]
            for str in strs[1:]:
                if str[i] != x:
                    return strs[0][:i]
        return strs[0][:minlength]


            


      
         
          