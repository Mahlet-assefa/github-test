class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        add, i = 1,0

        while add:
            if i<len(digits):
                if digits[i] == 9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    add=0
            else:
                digits.append(1)
                add=0
            i += 1
        return digits[::-1]