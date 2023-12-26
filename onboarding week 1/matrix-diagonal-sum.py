class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pmy_dict=defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i==len(mat)-j-1:
                    pmy_dict[i]+=mat[i][j]
        summed=0
        for value in pmy_dict.values():
            summed+=value
        return summed