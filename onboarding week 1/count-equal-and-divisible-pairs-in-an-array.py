class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        my_dict = defaultdict(list)
        for index,value in enumerate(nums):
            my_dict[value].append(index)
        print(my_dict)
        for index in my_dict.values():
            for i in range(len(index)): 
                for j in range(i + 1, len(index)):
                    if index[i] * index[j] % k == 0:
                        count+=1
        return count
       
            
            
            
           


            