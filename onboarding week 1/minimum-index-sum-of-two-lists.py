class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3=[value for value in list1 if value in list2]

        my_dict=dict()
        for i in list3:
          j=list1.index(i) + list2.index(i)
          if j not in my_dict:
            my_dict[j]=[i]
          else:
            my_dict[j].append(i)
        return my_dict[sorted(my_dict.keys())[0]]