class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict=defaultdict(int)
        res=0
        l = 0
  
        for r, val in enumerate(fruits):
            my_dict[val] += 1

            while len(my_dict) > 2:
                curr = fruits[l]
                if my_dict[curr] == 1:
                    del my_dict[curr]
                else:
                    my_dict[curr] -= 1

                l += 1
            res = max(res, r - l + 1)
    
        return res