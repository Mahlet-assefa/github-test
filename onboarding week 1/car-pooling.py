class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*1001
        for c,start,end in trips:
            arr[start]+=c
            arr[end]-=c
        print(arr)
        prefix=0
        for i in range(len(arr)):
            prefix+=arr[i]
            if prefix>capacity:
                return False
        return True
        
            