class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        max=0
        val=0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            if d[nums[i]] > max:
                max = d[nums[i]]
                val = nums[i]

        return val

          
           
            