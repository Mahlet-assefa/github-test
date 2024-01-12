class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        my_dict=defaultdict(int)
        res=0 
        ans=float("inf")
        for r in range(len(cards)):
            if cards[r] not in my_dict:
                my_dict[cards[r]]+=r
                #print(my_dict)
            else: 
                res = r - my_dict[cards[r]]+1
                my_dict[cards[r]]=r
                ans=min(res,ans)
        if res==0:
            return -1
        else:   
            return ans 
        
        



                
        #     else:
        #         my_set.add(cards[idx])
                
        # return -1
                
