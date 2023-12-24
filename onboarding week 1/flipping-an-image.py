class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i[:]=i[::-1]
            for j in range(len(i)):
                if i[j]==0:
                    i[j]=1
                elif i[j]==1:
                    i[j]=0
                  
        return image 