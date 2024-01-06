class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_val = sum(nums[0:k])
        max_val = sum_val
        for i in range(k,len(nums)):
            sum_val = sum_val - nums[i-k] + nums[i]
            max_val = max(max_val, sum_val)
        return max_val/k