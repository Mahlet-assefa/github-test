class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        ans=[]
        for r in range(len(arr1)):
            if not arr1[r] in arr2:
                res.append(arr1[r])
                res.sort()
                print(res)
        
        for j in range(len(arr2)):
            for i in range(len(arr1)):
                if arr2[j]==arr1[i]:
                    ans.append(arr1[i])
        ans+=res      
        return ans