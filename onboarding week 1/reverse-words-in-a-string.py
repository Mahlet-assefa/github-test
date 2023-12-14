class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        ans=""
        word = s.split(" ")
        print(word)
        for w in range(len(word)-1,-1,-1):
            if word[w]=='':
                pass
            else:
                res.append(word[w])
            ans= " ".join(res).strip()
        return ans
        
