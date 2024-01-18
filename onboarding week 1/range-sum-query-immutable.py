class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[0]
        self.summed=0
        for i in range(len(nums)):
            self.summed+=nums[i]
            self.prefix.append(self.summed)
            #print(self.prefix)
           

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left] 





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)