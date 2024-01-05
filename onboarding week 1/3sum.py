class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for l, a in enumerate(nums):
            if l>0 and a == nums[l-1]:
                continue
            i=l+1
            j= len(nums) - 1
            while i < j:
                    summed = a + nums[i] + nums[j]
                    if summed > 0:
                        j -= 1
                    elif summed < 0:
                        i += 1
                    else:
                        res.append([a, nums[i], nums[j]])
                        i += 1
                        while nums[i] == nums[i-1] and i < j:
                            i += 1
        return res

