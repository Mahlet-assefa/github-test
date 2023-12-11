class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans=[]
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        z = zip(positive, negative)

        for i, j in z:
            ans.append(i)
            ans.append(j)
        return ans