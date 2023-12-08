class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha={order[i]: i for i in range(len(order))}
        for i in range(1,len(words)):
            a, b = words[i-1], words[i]
            for j in range(len(a)):
                if j == len(b): 
                    return False
                aix, bix = alpha[a[j]], alpha[b[j]]
                if aix < bix: 
                    break
                if aix > bix: 
                    return False
        return True
             