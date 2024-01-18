class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        my_dict=defaultdict(int)
        my_dict[0]+=1
        for i in range(len(nums)):
            prefix+=nums[i]
            prefix=prefix%k
            cnt+=my_dict[prefix]
            #print(my_dict)
            my_dict[prefix]+=1
        return cnt
           
