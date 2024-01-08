class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_len=0
        j=0
        my_dict={x: 0 for x in nums}
        if 0 not in my_dict.keys():
            return n-1
        for i in range(n):
            my_dict[nums[i]]+=1

            if my_dict[0]>1:
                my_dict[nums[j]]-=1
                j+=1
            max_len = max(max_len, i-j)
        return (max_len)        
            
            
