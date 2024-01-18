class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        cnt=0
        my_dict=defaultdict(int)
        my_dict[0]+=1
        for i in range(len(nums)):
            prefix+=nums[i]
            cnt+=my_dict[prefix-goal]
            my_dict[prefix]+=1
        return cnt

