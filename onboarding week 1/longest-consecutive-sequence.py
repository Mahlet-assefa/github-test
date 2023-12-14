class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for num in s:
            if num - 1 not in s:
                cur_num = num
                cur = 1

                while cur_num + 1 in s:
                    cur_num += 1
                    cur += 1
                longest = max(longest, cur)

        return longest
 
        


    
 
       
 
 

            