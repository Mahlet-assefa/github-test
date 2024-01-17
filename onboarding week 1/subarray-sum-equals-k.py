class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        diff=0
        cnt=0
        my_dict=defaultdict(int)
        my_dict[0]+=1
        for i in range(len(nums)):
            prefix+=nums[i]
            cnt+=my_dict[prefix-k]
            my_dict[prefix]+=1
        return cnt
           

        # if diff in my_dict:
        #     cnt+=1
        # else:
        #     my_dict[diff]+=1
        # return cnt






















        
        
            
        # for j in range(len(arr)):   
        #     diff=arr[j]-k
        #     if diff in my_dict:
        #         cnt+=my_dict[arr[j]]
        #         print(cnt)
        #     else:
        #         my_dict[diff]+=1
        #         #print(my_dict) 
        # return cnt


            