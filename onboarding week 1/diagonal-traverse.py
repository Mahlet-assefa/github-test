class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict = defaultdict(list)
       
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key=i+j
                my_dict[key].append(mat[i][j])
        list1=[]
        for key in my_dict.items():
            if key[0]%2==0:
                list1.extend(key[1][::-1])
            else:
                list1.extend(key[1])
                        
        return list1

                
        # for index,value in enumerate(mat):
        #     my_dict[value].append(index)
        # print(my_dict)
            