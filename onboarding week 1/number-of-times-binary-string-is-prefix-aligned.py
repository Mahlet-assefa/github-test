class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt=0
        maxii=0
        for i in range(len(flips)):
            maxii= max(maxii,flips[i])
            if i+1==maxii:
                cnt+=1
        return cnt



        