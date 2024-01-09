class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float("inf")
        d=float("inf")
        diff=0
        i=0
        while i<len(nums)-2:
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    diff = nums[i] + nums[l] + nums[r] - target
                    if abs(diff) < d:
                        d = abs(diff)
                        result = nums[i] + nums[l] + nums[r]
                    if diff < 0:
                        l += 1
                    elif diff > 0:
                        r -= 1
                    else:
                        return target
            i += 1
        return result