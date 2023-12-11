class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict={}
        for i,j in enumerate(nums):
            my_dict[j]= i
        for j, k in operations:
            index= my_dict[j]
            nums[index]=k
            my_dict[k] = index
            del my_dict[j]
        return nums
