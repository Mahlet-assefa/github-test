class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            mini=max(firstList[i][0],secondList[j][0])
            maxi=min(firstList[i][1],secondList[j][1])
            if mini<=maxi:
                res.append([mini,maxi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res

