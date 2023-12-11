class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summed = sum(a for a in nums if a % 2 == 0)
        for operation, index in queries:
            if nums[index] % 2 == 0:
                summed -= nums[index]
            nums[index] += operation
            if nums[index] % 2 == 0:
                summed += nums[index]
            ans.append(summed)
        return ans