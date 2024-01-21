class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        my_dict = {}
        prefix = [0]*(len(nums)+1)
        res=0
        l = 0
        for r, num in enumerate(nums):
            prefix[r+1] = prefix[r]+num
            if num in my_dict:
                l = max(l, my_dict[num]+1)
            my_dict[num] = r
            res = max(res, prefix[r+1]-prefix[l])
        return res