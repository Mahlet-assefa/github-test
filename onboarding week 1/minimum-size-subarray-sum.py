class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summed=0
        res = float("inf")
        for r in range(len(nums)):
            summed += nums[r]
            while summed >= target:
                res = min(res,r-l+1)
                summed -= nums[l]
                l+=1
        if res == float("inf"):
            return 0 
        else:
            return res 