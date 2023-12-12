class Solution:
    def isHappy(self, n: int) -> bool:
        rem=0
        my_set=set()
        while(True):
            rem =0
            while(n>0):
                rem+=(n%10)**2
                n=n//10
            if rem == 1:
                return True

            if rem in my_set:
                return False
            my_set.add(rem)
            n=rem
                

    

        def sqr_nums(res):
            for i in res:
              yield i*i