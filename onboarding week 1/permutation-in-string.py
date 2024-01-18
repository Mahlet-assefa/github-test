class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_dict=collections.Counter(s1)
        n=len(s1)
        for i in range(len(s2)):
            if my_dict[s2[i]]>0:
                n-=1
            my_dict[s2[i]]-=1
            if n==0:
                return True
            start = i + 1 - len(s1)
            if start >= 0:
                my_dict[s2[start]] += 1
                if my_dict[s2[start]] > 0:
                    n += 1
        return False
        

            