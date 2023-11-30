class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0

        if x<0:
            return False
        while temp>0:
            dig= temp%10
            rev= rev*10 + dig
            temp//=10
        if rev == x:
            return True
        else:
            return False