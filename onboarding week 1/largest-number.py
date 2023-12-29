class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=""
        def comparator(a,b):
            ans1= int(str(a)+str(b))
            ans2= int(str(b)+str(a))
            if ans1<ans2:
                return True
            else:
                return False
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if comparator(nums[j],nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        
        
        for i in nums:
            res += str(i)   

        return str(int(res))




