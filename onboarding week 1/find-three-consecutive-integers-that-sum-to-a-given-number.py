class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if num % 3 == 0:
            x = num // 3
            arr=[x-1,x,x+1]
            return arr
        else:
            return []
            