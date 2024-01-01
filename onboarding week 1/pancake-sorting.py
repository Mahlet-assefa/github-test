class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr) - 1, -1, -1):
            i = arr.index(max(arr[:x + 1]))
            arr[:i + 1] = arr[:i + 1][::-1]
            res.append(i + 1)
            arr[:x + 1] = arr[:x + 1][::-1]
            res.append(x + 1)

        return res

       

