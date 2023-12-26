class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        my_dict=dict(zip(names,heights)) 
            
        #print(my_dict)

        for i in range(len(names)-1,-1,-1):
           for j in range(i):
             if heights[j] < heights[j+1]:
                temp=names[j]
                names[j]=names[j+1]
                names[j+1]=temp
                heights[j],heights[j+1]=heights[j+1],heights[j]
        return names
        # res=[]
        # for key,value in my_dict.items():
        #    res.append(key)
        # return res
        


