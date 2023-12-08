class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hasht = {}
        missing = -1

        for num in nums:
            if num in hasht:
                pass
            else:
                hasht[num] = True

        for i in range(len(nums) + 1):
            if i not in hasht:
                missing = i
                break

        return missing