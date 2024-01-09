class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxi=0
        for i,val in enumerate(nums):
            if nums[i]==0:
                k=k-1
            if k<0:
                if nums[l]==0:
                    k+=1
                else:
                    k=k
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi


