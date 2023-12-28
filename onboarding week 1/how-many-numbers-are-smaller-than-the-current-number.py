class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       count = collections.Counter(nums)
       #print(count)
       for i in range(max(nums)+1):
            count[i] += count[i-1]
       return [count[i-1] for i in nums]
