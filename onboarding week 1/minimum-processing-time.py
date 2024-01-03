class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        summed=0
        res=0
        i=0
        j=0
        while i<len(tasks) and j<len(processorTime):
               summed=tasks[i]+processorTime[j]
               res=max(res,summed)
               i+=4
               j+=1
        return res

                    

