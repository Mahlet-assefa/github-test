class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        max=(len(arr)*25)//100
        val=0
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
            if d[arr[i]] >= max:
                max = d[arr[i]]
                val = arr[i]

        return val

        
        