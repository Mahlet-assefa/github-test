class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counting=0
        summed=0
        n=len(costs)-1
        mini=min(costs)
        maxi=max(costs)
        r=maxi-mini
        res=[0]*n
        count=[0]*(r+1)

        for i in costs:
            count[i-mini]+=1
        s=0
        for i in range(r+1):
            for j in range(count[i]):
                costs[s]=i+mini
                s+=1
        #print(costs)
        for i in costs:
            if coins-i >= 0:
                    counting+=1
                    coins-=i
            else:
                break
        return counting


    


        

