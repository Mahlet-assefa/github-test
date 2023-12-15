class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict={}
        for path in paths:
            parsed = path.split()
            directory= parsed[0] + "/"
            l=0
            for i in parsed[1:]:
                l=i.index("(")
                file=i[l:-1]
                if file in my_dict:
                    my_dict[file].append(directory+i[:l])
                else:
                    my_dict[file]=[directory + i[:l] ]
        res=[]
        for j in my_dict:
            if len(my_dict[j])>1:
                res.append(my_dict[j])
        return res
