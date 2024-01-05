class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
       diff=0
       store=0
       points=sorted(points,key=lambda x:x[0])
       print(points)
       for i in range(len(points)-1):
            diff = points[i+1][0] - points[i][0]
            store = max(store,diff)
       return store