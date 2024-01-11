class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = collections.Counter(p)
        slice_str = s[: len(p)]
        sdict = collections.Counter(slice_str)

        res = []

        for r in range(0, len(s) - len(p) + 1):
            if r > 0:
                sdict[s[r - 1]] -= 1
                print(sdict)
                sdict[s[r + len(p) - 1]] += 1

                if sdict[s[r - 1]] == 0:
                    del sdict[s[r - 1]]

            if len(sdict) == len(pdict):
                if sdict == pdict:
                    res.append(r)

        return res