class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=0
        suffix=0
        idx=-1
        for i in range(0,len(nums)):
            prefix+=nums[i]
            suffix=sum(nums[i:])
            if prefix==suffix:
                idx=i
                break
        return idx
            
        
        
