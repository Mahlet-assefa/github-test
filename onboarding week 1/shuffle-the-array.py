class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans1=[]
        ans2=[]
        output=[]

        for i in range(len(nums)):
            if i<len(nums)//2:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        z = zip(ans1, ans2)
        for i, j in z:
            output.append(i)
            output.append(j)
        return output


        
